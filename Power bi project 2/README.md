# 🏥 Healthcare Monitoring Dashboard - Power BI Project

[![Power BI](https://img.shields.io/badge/Power%20BI-Desktop-yellow.svg)](https://powerbi.microsoft.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Data Science](https://img.shields.io/badge/Data-Analytics-green.svg)](https://github.com/praneesh-sns/healthcare-monitoring-dashboard)

> **Complete Power BI solution for hospital healthcare monitoring system with real-time patient vitals, doctor performance tracking, and resource utilization analytics.**

## 📋 Project Overview

This comprehensive Power BI project creates an interactive healthcare monitoring dashboard for hospital administration and clinical staff. The solution tracks **1,200+ patient records** with time-series vitals data, department workloads, ICU utilization, emergency case management, and doctor performance metrics.

### 🎯 Key Features
- **Real-time Patient Monitoring**: Heart rate, blood pressure, oxygen saturation, temperature tracking
- **Resource Management**: Bed occupancy, ICU utilization, ward capacity analysis  
- **Doctor Performance**: Patient load, treatment duration, rating analytics
- **Emergency Analytics**: Critical case tracking, department-wise emergency trends
- **Interactive Dashboards**: 6 comprehensive dashboard pages with 30+ DAX measures

## 🗂️ Project Structure

```
healthcare-monitoring-dashboard/
│
├── 📁 data/
│   ├── healthcare_data.csv          # Main dataset (1,200 patient records)
│   ├── data_dictionary.md           # Field descriptions and data types
│   └── sample_data.csv              # Sample subset for testing
│
├── 📁 powerbi/
│   ├── Healthcare_Dashboard.pbix    # Main Power BI file
│   ├── dax_formulas.txt            # All DAX measures and calculations
│   └── visual_guidelines.md        # Dashboard design specifications
│
├── 📁 documentation/
│   ├── project_report.md           # Complete project documentation
│   ├── setup_guide.md              # Installation and setup instructions
│   ├── user_manual.md              # Dashboard usage guide
│   └── insights_analysis.md        # Key findings and recommendations
│
├── 📁 screenshots/
│   ├── dashboard_overview.png      # Main dashboard screenshot
│   ├── vitals_monitoring.png       # Patient vitals page
│   ├── doctor_performance.png      # Doctor analytics page
│   └── ward_utilization.png        # Ward management page
│
├── 📁 scripts/
│   ├── data_generator.py           # Dataset generation script
│   └── data_validation.py          # Data quality checks
│
├── README.md                       # Project overview (this file)
├── LICENSE                         # MIT License
├── .gitignore                      # Git ignore file
└── requirements.txt                # Python dependencies
```

## 🚀 Quick Start

### Prerequisites
- Power BI Desktop (latest version)
- Microsoft Excel (optional, for data viewing)
- Python 3.8+ (for data generation scripts)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/praneesh-sns/healthcare-monitoring-dashboard.git
   cd healthcare-monitoring-dashboard
   ```

2. **Open Power BI Desktop**
   - Launch Power BI Desktop
   - Open `powerbi/Healthcare_Dashboard.pbix`
   - Refresh data connections if prompted

3. **Load the dataset**
   - Data source: `data/healthcare_data.csv`
   - Power Query will automatically transform data types
   - All DAX measures are pre-configured

4. **Explore the dashboards**
   - Navigate through 6 interactive pages
   - Use slicers for filtering (Department, Date Range, Demographics)
   - Hover over visuals for detailed tooltips

## 📊 Dashboard Pages

### 1. 🏥 **Overview Dashboard**
- **KPI Cards**: Total patients, bed occupancy, ICU utilization, emergency cases
- **Department Workload**: Horizontal bar chart showing patient distribution
- **Monthly Trends**: Admission and discharge patterns throughout 2024

### 2. 💓 **Patient Vitals Monitoring**
- **Vitals Cards**: Real-time heart rate, blood pressure, SpO2, temperature
- **Trend Analysis**: Time-series vitals tracking with anomaly detection
- **Critical Alerts**: Conditional formatting for abnormal vitals
- **Filters**: Age group, gender, ward, treatment status

### 3. 👨‍⚕️ **Doctor Performance Analytics**
- **Performance Table**: Doctor rankings by patient count and ratings
- **Scatter Plot**: Patient load vs. average treatment duration
- **Rating Distribution**: Doctor feedback analysis
- **Workload Balance**: Department-wise doctor allocation

### 4. 🏢 **Ward Utilization & Capacity**
- **Occupancy Rates**: Ward-wise bed utilization vs. capacity
- **Heat Map**: Time-based utilization patterns (hourly/daily)
- **Capacity Alerts**: Color-coded warnings for overcapacity
- **Utilization Trends**: Historical occupancy patterns

### 5. 🚨 **Emergency & Critical Cases**
- **Emergency Overview**: Total emergency cases with trend analysis
- **Department Breakdown**: Pie chart of emergency cases by department
- **Critical Status Tracking**: ICU admissions and critical patient monitoring
- **Time Analysis**: Peak emergency hours and seasonal patterns

### 6. 📈 **Analytics & Insights**
- **Treatment Outcomes**: Recovery rates and length of stay analysis
- **Predictive Indicators**: Readmission risk factors
- **Resource Optimization**: Recommendations for capacity planning
- **Cost Analysis**: Treatment cost per department and doctor

## 📋 Key Metrics & KPIs

| Metric | Current Value | Target | Status |
|--------|---------------|---------|---------|
| **Total Patients** | 1,200 | - | ✅ |
| **Bed Occupancy Rate** | 85% | < 90% | ✅ |
| **ICU Utilization** | 35.7% | < 80% | ✅ |
| **Emergency Cases** | 30.2% | < 35% | ✅ |
| **Average LOS** | 15.8 days | < 18 days | ✅ |
| **Doctor Rating** | 4.2/5.0 | > 4.0 | ✅ |

## 🔍 Key Insights

1. **Peak Activity**: ICU usage spikes **55% on weekends** vs. 35% weekday average
2. **Emergency Patterns**: **29% of admissions are emergencies** with peak times 20:00-23:00
3. **Department Efficiency**: Surgery shows **highest throughput** (14% of patients, shortest LOS)
4. **Resource Optimization**: **Ward C is 12% underutilized** - opportunity for reallocation
5. **Clinical Alert**: **21% of adult patients** show hypertension (BP > 140/90)

## 🛠️ Technical Implementation

### DAX Formulas (30+ Measures)
```dax
Total_Patients = COUNTROWS('Healthcare Data')
Bed_Occupancy_Rate = DIVIDE([Currently_Admitted], [Total_Patients], 0) * 100
ICU_Utilization_Rate = DIVIDE([ICU_Patients], [Total_Patients], 0) * 100
Emergency_Rate = DIVIDE([Emergency_Cases], [Total_Patients], 0) * 100
Avg_Treatment_Days = AVERAGE('Healthcare Data'[TreatmentDays])
```

### Data Model
- **Fact Table**: Healthcare Data (1,200 rows × 22 columns)
- **Dimension Tables**: Date, Doctor, Department, Ward
- **Relationships**: Star schema with optimized performance
- **Measures**: 30+ DAX calculations for KPIs and analytics

## 👥 Team & Credits

**Project Lead**: Praneesh S  
**Institution**: SNS College of Engineering  
**Internship**: Infotact Solution - Data Analytics Intern  
**Supervisor**: [Supervisor Name]  

### 🙏 Acknowledgments
- Microsoft Power BI Documentation
- Healthcare Industry Standards (HL7, FHIR)
- Perplexity Pro Labs for dataset generation
- SNS College of Engineering for project support

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📞 Contact & Support

- **Email**: praneesh.sns@example.com
- **LinkedIn**: [Praneesh S](https://linkedin.com/in/praneesh-sns)
- **Project Issues**: [GitHub Issues](https://github.com/praneesh-sns/healthcare-monitoring-dashboard/issues)

---

## 🎯 Next Steps

- [ ] **Real-time Integration**: Connect to hospital management systems
- [ ] **Predictive Analytics**: ML models for readmission risk prediction  
- [ ] **Mobile Optimization**: Power BI mobile app optimization
- [ ] **IoT Integration**: Live vitals streaming from bedside monitors
- [ ] **Advanced Analytics**: Patient flow optimization algorithms

---

⭐ **If this project helped you, please give it a star!** ⭐

**Last Updated**: July 2025  
**Version**: 1.0.0