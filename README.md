# automated-quality-check
3D_Inspection_System/
│
├── 01_Environment/
│   ├── requirements.txt
│   ├── environment.yml
│   └── setup_instructions.md
│
├── 02_Data/
│   ├── 01_CAD_References/
│   │   ├── original/                    # Original CAD files (.step, .iges)
│   │   ├── converted/                   # Converted to STL/PLY format
│   │   └── metadata/                    # CAD file specifications
│   │
│   ├── 02_Scanned_Data/
│   │   ├── raw/                         # Unprocessed scan files
│   │   │   ├── 2025-06-19_part001_scan001.ply
│   │   │   ├── 2025-06-19_part001_scan002.ply
│   │   │   └── ...
│   │   ├── preprocessed/                # Cleaned, filtered scans
│   │   └── aligned/                     # ICP-aligned scan data
│   │
│   ├── 03_Sample_Datasets/
│   │   ├── test_parts/                  # Sample parts for testing
│   │   ├── calibration/                 # Calibration artifacts
│   │   └── validation/                  # Known good/bad samples
│   │
│   └── 04_Archives/
│       ├── daily_backups/
│       └── project_snapshots/
│
├── 03_Software/
│   ├── 01_CloudCompare/
│   │   ├── installation/
│   │   ├── plugins/
│   │   └── scripts/
│   │
│   ├── 02_Python_Scripts/
│   │   ├── data_preprocessing/
│   │   ├── alignment_algorithms/
│   │   ├── deviation_analysis/
│   │   └── report_generation/
│   │
│   └── 03_Automation/
│       ├── batch_processing/
│       ├── file_monitoring/
│       └── quality_control/
│
├── 04_Configuration/
│   ├── cloudcompare_settings.xml
│   ├── icp_parameters.json
│   ├── scan_preprocessing_config.yml
│   └── report_templates/
│
├── 05_Documentation/
│   ├── setup_guides/
│   ├── user_manuals/
│   ├── api_documentation/
│   └── troubleshooting/
│
├── 06_Results/
│   ├── inspection_reports/
│   │   ├── pdf_reports/
│   │   ├── csv_data/
│   │   └── visualization/
│   │
│   ├── deviation_analysis/
│   │   ├── heatmaps/
│   │   ├── statistical_summaries/
│   │   └── trend_analysis/
│   │
│   └── quality_metrics/
│       ├── accuracy_assessments/
│       └── performance_benchmarks/
│
├── 07_Tools/
│   ├── calibration_utilities/
│   ├── format_converters/
│   ├── data_validators/
│   └── performance_monitors/
│
└── 08_Logs/
    ├── processing_logs/
    ├── error_logs/
    └── audit_trails/
