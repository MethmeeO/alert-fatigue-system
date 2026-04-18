Web Application Alert Fatigue Reduction System
AI-Powered Detection & Forensic Prioritization Architecture

The Concept

In modern SOC environments, analysts are overwhelmed by thousands of daily logs.
.HEIST - High-Efficiency Intelligent Security Tracker) uses Machine Learning to filter background noise and highlight actual security incidents.

Key AI Features

Deep Learning Anomalies = Uses an Autoencoder (PyTorch) to detect "unseen" attack patterns.
Intelligent Clustering  = Employs DBSCAN to group similar alerts, preventing analysts from seeing the same attack 100 times
Dynamic Risk Scoring    =  Moves beyond static rules to calculate risk based on behavior and Threat Intelligence.

 Forensic Capabilities
 
 Multi-Source Correlation     =  Unifies `App`, `Auth`, and `WAF` logs for a single source of truth.
Automated Artifact Extraction = Pulls IPs, Endpoints, and User Behaviors for immediate forensic review.
Threat Intel Integration      =  Cross-references logs with real-world threat databases to identify known malicious actors.

 Project Structure
```text
├── src/
│   ├── preprocessing/   # Data Forensic Cleaning & Normalization
│   ├── models/          # ML Pipeline (DBSCAN & Autoencoders)
│   └── threat_intel.py  # IP Reputation & OSINT Checks
├── logs/                # Raw Security Log Storage
├── data/                # Processed Forensic Outputs
└── main.py              # System Orchestrator
