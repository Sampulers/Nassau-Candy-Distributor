# 1. Title
**Factory Reallocation & Shipping Optimization Recommendation System for Nassau Candy Distributor**
AI-Powered Factory Assignment, Logistics Optimization and Decision Intelligence Platform for Nassau Candy Distributor
"https://github.com/Sampulers/Nassau-Candy-Distributor/blob/8ad0ab6180641ba061fddf06c9994ad282aaeee9/1.png"

# 2. Summary
An AI-driven supply chain decision intelligence platform that predicts delivery lead time, optimizes factory-product assignments using machine learning and mixed-integer optimization, and recommends cost-efficient factory reallocations to improve logistics performance.

# 3. Overview
**Business Background**
Nassau Candy Distributor operates a nationwide supply chain where multiple factories manufacture and ship confectionery products to customers across different regions. Traditionally, products are assigned to factories using static business rules and legacy operational practices. While this approach supports day-to-day operations, it does not account for changing customer demand, transportation distances, shipping costs, or factory utilization.
To remain competitive, leadership requires a data-driven decision support system capable of answering:

| **"What should we change to improve logistics performance while maintaining profitability?"**
This project introduces an AI-powered Decision Intelligence System that:

● Predicts shipping outcomes under different factory assignment scenarios.
● Recommends optimal product reallocations across factories.
● Balances shipping efficiency, operational performance, and profitability.

**Current Logistics Workflow**
Currently, Nassau Candy assigns products to manufacturing facilities using predefined factory-product mappings without dynamically considering transportation distance, regional demand, or logistics performance.

As a result, the existing workflow leads to:
● Suboptimal shipping distances.
● Higher delivery lead times for certain customer regions.
● Increased transportation costs.
● Margin erosion caused by logistics inefficiencies.
● Uneven factory workload distribution.

**Existing Challenges**
The current logistics planning process lacks an intelligent decision-support framework capable of evaluating alternative operational strategies before implementation.

Specifically, there is no system to:
● Simulate factory–product reassignment scenarios
● Quantify the operational impact before execution
● Compare multiple allocation strategies.
● Recommend optimal factory configurations at scale.
● Support data-driven logistics planning.
  
**Why Factory Reallocation is Necessary**
As customer demand, transportation costs, and regional shipping patterns continue to change, static factory assignments become increasingly inefficient. A product manufactured at one factory may reach certain customer regions faster and at a lower cost if produced by another facility.

Factory reallocation enables the organization to:

● Reduce transportation distance.
● Minimize delivery lead times.
● Lower shipping and operational costs.
● Improve factory utilization.
● Increase overall supply chain efficiency.
● Support strategic, data-driven operational decisions.

**Objectives of the Project**

The primary objective of this project is to develop an AI-powered Factory Reallocation & Shipping Optimization Decision Intelligence System capable of:
● Predicting delivery lead time using machine learning.
● Simulating alternative factory-product assignment scenarios.
● Optimizing factory allocation using mathematical optimization techniques.
● Recommending optimal factory-product combinations.
● Identifying high-risk shipping routes.
● Evaluating operational impact before implementation.
● Improving logistics efficiency while maintaining profitability.
● Providing interactive decision support through Power BI dashboards and scenario simulation.

**Expected business impact**

"https://github.com/Sampulers/Nassau-Candy-Distributor/blob/3b5c48378bf685ad97b7c7cb5d4157bb4ae088be/Copilot_20260625_040851.png"

# 4. Problem Statement
Current process relies on static factory assignments.
Problems:
● Long transportation distance
● Higher shipping cost
● Poor factory utilization
● Longer lead times
● No simulation capability
● No recommendation engine
● No optimization before implementation

# 5. Dataset
Source: "Nassau Candy Distributor Supply Chain Dataset"
Dataset Fields Description:
Field	Description
Row ID	                           Unique row identifier
Order ID	                         Unique order identifier
Order Date	                       Date of order
Ship Date	                         Date of shipment
Ship Mode	                         Shipping method of order
Customer ID	                       Unique customer identifier
Country/Region	                   Country or region of customer
City	                             City of customer
State/Province	                   State/province of customer
Postal Code	                       Postal code / zip code of customer
Division	                         Product division
Region	                           Region of customer
Product ID	                       Unique product identifier
Product Name	                     Product long namer
Sales	                             Total sales value of order
Units	                             Total units of order
Gross Profit	                     Gross profit of order ( Sales - Cost )
Cost	                             Cost to manufacture

**Table of engineered features**:

| Current Distance   | Optimized Distance   |
| Lead Time          | Distance Saved       |
| Factory Profit     | Confidence Score     |
| Risk Level         | Capacity Stress      |
| Potential Profit   |

# 6. Tools & Technologies

| Category         | Tools                                      |
| ---------------- | ------------------------------------------ |
| Language         | Python                                     |
| Data Processing  | Pandas, NumPy                              |
| Visualization    | Matplotlib, Plotly                         |
| Machine Learning | XGBoost, LightGBM, CatBoost, Random Forest |
| Explainability   | SHAP                                       |
| Optimization     | PuLP (MILP)                                |
| Dashboard        | Power BI                                   |
| Deployment       | Streamlit                                  |
| Version Control  | GitHub                                     |

# 7. Methods
Raw Dataset
      │
      ▼
Data Cleaning
      │
      ▼
EDA
      │
      ▼
Feature Engineering
      │
      ▼
Geospatial Distance Calculation
      │
      ▼
Lead Time Prediction
      │
      ▼
SHAP Analysis
      │
      ▼
Factory Reallocation Simulation
      │
      ▼
MILP Optimization
      │
      ▼
Recommendation Engine
      │
      ▼
Power BI Dashboard

# 8. Key Insights
Summarize findings:
● Shipping distance strongly influences lead time.
● Factory utilization varies significantly.
● Product reassignment can reduce logistics costs.
● High-risk routes are concentrated in specific regions.
● Optimization identifies alternative factories with lower transportation costs while maintaining service levels.

Include one or two visuals from your Route Performance and Risk pages.

# 9. Dashboard / Model / Output

Executive Overview
(Insert Screenshot 1)

Shipping Performance Analytics

(Insert Screenshot 2)

Machine Learning Prediction Dashboard

(Insert Screenshot 3)

Route & Product Clustering

(Insert Screenshot 4)

What-if Scenario Simulator

(Insert Screenshot 5)

Optimization Recommendation Engine

(Insert Screenshot 6)

Risk & Impact Analysis

(Insert Screenshot 7)

**File	Description**

| lead_time_predictions.xlsx	  | Predicted lead times for all scenarios |
| lead_time_metrics.xlsx	      | Evaluation metrics (MAE, RMSE, R²)     |
| shap_output.xlsx	|           | SHAP feature importance values         |
| Nassau_Candy_Distributor.pbix	| Interactive Power BI dashboard         |

# 10. How to Run this Project
1. Clone the repository.
2. Install Python dependencies.
3. Place the dataset and ZIP lookup file in the Data folder.
4. Run the Jupyter notebook to generate predictions and optimization outputs.
5. Review the generated Excel files.
6. Open the Power BI report to explore dashboards.
7. Launch the Streamlit application for interactive scenario simulation.

# 11. Results & Conclusion
Summarize the achievements:
● Developed a predictive lead-time model.
● Built a geospatial logistics analysis framework.
● Implemented factory-product reassignment simulation.
● Applied MILP optimization for recommendation generation.
● Delivered a Power BI decision-support dashboard.
● Produced actionable recommendations to improve shipping efficiency and profitability.   

# 12. Future Work
Suggested enhancements:
● Real-time ERP integration (SAP/Oracle).
● Live GPS and shipment tracking.
● Reinforcement learning for adaptive routing.
● Vehicle Routing Problem (VRP) optimization.
● Demand forecasting integration.
● Carbon emission optimization.
● Digital twin for supply chain simulation.
● Multi-objective optimization balancing cost, time, and sustainability.

**System Architecture Diagram**
                    ┌────────────────────────────┐
                    │   Nassau Candy Dataset     │
                    └─────────────┬──────────────┘
                                  │
                                  ▼
                    ┌────────────────────────────┐
                    │ Data Cleaning & Validation │
                    └─────────────┬──────────────┘
                                  │
                                  ▼
                    ┌────────────────────────────┐
                    │ Feature Engineering        │
                    │ • Distance                │
                    │ • Coordinates             │
                    │ • Profit                  │
                    │ • Risk                    │
                    └─────────────┬──────────────┘
                                  │
             ┌────────────────────┼────────────────────┐
             ▼                    ▼                    ▼
      ML Prediction         SHAP Explainability    Route Clustering
             │                    │                    │
             └────────────────────┼────────────────────┘
                                  ▼
                  Factory Reallocation Simulation
                                  │
                                  ▼
                    MILP Optimization (PuLP)
                                  │
                                  ▼
                     Recommendation Engine
                                  │
                                  ▼
         Power BI Dashboard + Streamlit Application
                                  │
                                  ▼
                    Business Decision Support
