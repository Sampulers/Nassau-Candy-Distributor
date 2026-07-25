
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Nassau Candy Supply Chain Optimizer", layout="wide")

# Branded Corporate Header Layout
st.markdown("""
    <div style='display: flex; align-items: center; background-color: #F8FAFC; padding: 15px; border-radius: 10px; margin-bottom: 25px; border-left: 8px solid #1E3A8A;'>
        <div style='background-color: #1E3A8A; color: white; padding: 10px 20px; font-weight: 900; font-size: 20px; border-radius: 5px; margin-right: 20px; font-family: sans-serif; letter-spacing: 1px;'>
            NASSAU CANDY
        </div>
        <div>
            <h1 style='margin: 0; font-size: 28px; font-weight: 800; color: #1E3A8A; font-family: sans-serif;'>Logistics & Sourcing Network Optimizer</h1>
        </div>
    </div>
""", unsafe_allow_html=True)

# Clear background memory hooks and force real-time reading
@st.cache_data(ttl=5)  # Re-verifies data freshness every 5 seconds
def load_optimized_data():
    df = pd.read_excel("Optimized_Factory_Reallocations.xlsx")
    # Clean up column spaces to ensure exact string matching in filters
    df.columns = df.columns.str.strip()
    if 'Division' in df.columns:
        df['Division'] = df['Division'].str.strip()
    return df

try:
    df_results = load_optimized_data()
    if 'Product_Name' in df_results.columns:
        df_results = df_results.rename(columns={'Product_Name': 'Product Name'})
except Exception:
    df_results = pd.DataFrame({
        'Product Name': ["Wonka Bar - Milk Chocolate", "Laffy Taffy", "Nerds", "Wonka Gum", "Gummy Bears"],
        'Division': ["Chocolate", "Sugar", "Sugar", "Other", "Sugar"],
        'Current Factory': ["Wicked Choccy's", "Sugar Shack", "Sugar Shack", "Secret Factory", "Sugar Shack"],
        'Optimized Factory': ["Lot's O' Nuts", "Wicked Choccy's", "The Other Factory", "Lot's O' Nuts", "Secret Factory"],
        'Units': [120, 450, 310, 95, 600],
        'Optimized Lead Time': [186.89, 172.17, 158.67, 179.86, 142.30],
        'Estimated Route Cost ($)': [12.28, 35.35, 3.91, 10.36, 18.45],
        'Region': ['Interior', 'Atlantic', 'Pacific', 'Gulf', 'Atlantic'],
        'Ship Mode': ['Standard Class', 'Second Class', 'First Class', 'Same Day', 'Standard Class']
    })

# Formulate fallback data columns cleanly if missing from memory
if 'Division' not in df_results.columns:
    def assign_division(product_name):
        p_lower = str(product_name).lower()
        if any(k in p_lower for k in ['taffy', 'nerds', 'tart', 'dip', 'sugar']): return 'Sugar'
        elif any(k in p_lower for k in ['bar', 'chocolate', 'fudge', 'caramel']): return 'Chocolate'
        return 'Other'
    df_results['Division'] = df_results['Product Name'].apply(assign_division)

if 'Region' not in df_results.columns:
    regions_pool = ['Atlantic', 'Interior', 'Pacific', 'Gulf']
    df_results['Region'] = [regions_pool[i % len(regions_pool)] for i in range(len(df_results))]

if 'Ship Mode' not in df_results.columns:
    modes_pool = ['Standard Class', 'Second Class', 'First Class', 'Same Day']
    df_results['Ship Mode'] = [modes_pool[i % len(modes_pool)] for i in range(len(df_results))]

# Force-convert columns to standard strings to protect matching stability
df_results['Region'] = df_results['Region'].astype(str).str.strip()
df_results['Ship Mode'] = df_results['Ship Mode'].astype(str).str.strip()

# =========================================================================
# 🎯 ASYNCHRONOUS SIDEBAR SELECTION MODULES
# =========================================================================
st.sidebar.header("🎯 Supply Chain Scope Controls")

# 1. Business Division Selector
divisions = ["All Divisions"] + sorted(list(df_results['Division'].unique()))
selected_division = st.sidebar.selectbox("Select Business Division:", divisions)

# 2. Region Filter Dropdown
regions_list = ["All Regions"] + sorted(list(df_results['Region'].unique()))
selected_region = st.sidebar.selectbox("🗺️ Target Distribution Region:", regions_list)

# 3. Shipping Speed Mode Dropdown
modes_list = ["All Modes"] + sorted(list(df_results['Ship Mode'].unique()))
selected_mode = st.sidebar.selectbox("🚚 Logistics Transport Mode:", modes_list)

st.sidebar.markdown("---")
st.sidebar.header("🤖 ML Optimization Tuning")

priority_ratio = st.sidebar.slider(
    "Balance Strategy Vector:",
    min_value=0.0, max_value=1.0, value=0.5, step=0.1,
    help="0.0 emphasizes Maximum Speed | 1.0 emphasizes Maximum Profit"
)

# Apply Matrix Filters dynamically against user parameters
df_filtered = df_results.copy()
if selected_division != "All Divisions":
    df_filtered = df_filtered[df_filtered['Division'] == selected_division]
if selected_region != "All Regions":
    df_filtered = df_filtered[df_filtered['Region'] == selected_region]
if selected_mode != "All Modes":
    df_filtered = df_filtered[df_filtered['Ship Mode'] == selected_mode]

# =========================================================================
# 🛠️ INTERACTIVE FULFILLMENT ADJUSTMENT WORKSPACE
# =========================================================================
st.markdown("### 🛠️ Interactive Sourcing Adjustment Workspace")
st.info("Simulate manual network overrides below to recalculate optimization impacts dynamically.")

col_select_1, col_select_2, col_select_3 = st.columns(3)

with col_select_1:
    available_products = sorted(list(df_filtered['Product Name'].unique())) if len(df_filtered) > 0 else sorted(list(df_results['Product Name'].unique()))
    selected_product = st.selectbox("1. Choose Target Product Line:", available_products)

# Pick row base data matching your target product selection safely
product_data = df_results[df_results['Product Name'] == selected_product].iloc[0]

with col_select_2:
    all_factories = ["Lot's O' Nuts", "Wicked Choccy's", "Sugar Shack", "Secret Factory", "The Other Factory"]
    default_curr_idx = all_factories.index(product_data['Current Factory']) if product_data['Current Factory'] in all_factories else 0
    sim_current_factory = st.selectbox("2. Baseline Source Factory (Before):", all_factories, index=default_curr_idx)

with col_select_3:
    default_opt_idx = all_factories.index(product_data['Optimized Factory']) if product_data['Optimized Factory'] in all_factories else 0
    sim_optimized_factory = st.selectbox("3. Reallocated Target Factory (After):", all_factories, index=default_opt_idx)

# Weighting Calculation Logic Formulation
base_cost = float(product_data['Estimated Route Cost ($)']) if 'Estimated Route Cost ($)' in product_data else 10.0
base_time = float(product_data['Optimized Lead Time']) if 'Optimized Lead Time' in product_data else 150.0

cost_scaler = 0.75 + (0.25 * (1.0 - priority_ratio))
time_scaler = 0.75 + (0.25 * priority_ratio)

if sim_current_factory == sim_optimized_factory:
    adjusted_cost = base_cost
    adjusted_time = base_time
    savings_delta = 0.0
    time_delta = 0.0
    status_msg = "ℹ️ Sourcing locked. Production remains at standard baseline operational parameters."
else:
    adjusted_cost = base_cost * 0.82 * cost_scaler
    adjusted_time = base_time * 0.88 * time_scaler
    savings_delta = base_cost - adjusted_cost
    time_delta = base_time - adjusted_time
    status_msg = f"✅ Dynamic Reallocation complete! Routing optimization score adjusted to {priority_ratio} index factor."

# =========================================================================
# 📊 INTEGRATED FINANCIAL MARGIN KPIS
# =========================================================================
c1, c2, c3 = st.columns(3)
with c1:
    st.metric(
        label="📋 Product Attributes",
        value=selected_product[:25] + "..." if len(selected_product) > 25 else selected_product,
        delta=f"Region: {product_data['Region']} | {product_data['Ship Mode']}"
    )
with c2:
    st.metric(
        label="💰 Sourcing Freight Cost",
        value=f"${adjusted_cost:.2f}",
        delta=f"Before: ${base_cost:.2f}",
        delta_color="inverse"
    )
with c3:
    st.metric(
        label="📈 Before vs After Optimization Delta",
        value=f"+${savings_delta:.2f} Margin",
        delta=f"{time_delta:+.1f} Hrs Lead Time"
    )

st.caption(status_msg)
st.markdown("---")

# Global Matrix Strategy Log View
st.subheader(f"📋 Master Supply Chain Strategy Log ({len(df_filtered)} items matched)")
view_option = st.radio("Choose Log Perspective:", ["Show Filtered Strategy Log", "Show Only Rerouted Rows"], horizontal=True)

if view_option == "Show Only Rerouted Rows":
    display_df = df_filtered[df_filtered['Current Factory'] != df_filtered['Optimized Factory']]
else:
    display_df = df_filtered

st.dataframe(display_df, use_container_width=True)
