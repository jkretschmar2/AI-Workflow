# AI Process Workflow - Mermaid Diagrams

This repository contains Mermaid diagram files, data files, and forms documenting the AI Software Request and Governance process workflow at Teledyne.

## � Table of Contents

- [Introduction](#introduction)
- [Tech Stack](#tech-stack)
- [Repository Structure](#-repository-structure)
- [Directory Navigation](#-directory-navigation)
- [Main Files](#-main-files)
- [Process Flow Overview](#-process-flow-overview)
- [Viewing the Diagrams](#-viewing-the-diagrams)
- [Documentation](#-documentation)
- [Styling Guide](#-styling-guide)
- [Contributing](#-contributing)
- [Support](#-support)

## Introduction

This project was created to document and standardize the AI Software Request governance process at Teledyne. It provides visual process flows, data tracking, and assessment templates to ensure consistent evaluation and approval of AI tools and projects across the organization.

**Who is this for?**
- AI Governance Committee members
- Business unit leaders requesting AI tools
- IT and Security teams reviewing AI requests
- Developers maintaining process documentation

## 🛠️ Tech Stack

- **Mermaid** - Diagram-as-code for flowcharts and journey maps
- **JSON** - Data storage for tools, projects, and initiatives
- **Markdown** - Documentation format
- **HTML/CSS/JS** - Static site for web viewing (docs/)
- **PowerShell** - Build scripts
- **Git/GitHub** - Version control and collaboration

## �📁 Repository Structure

```
AI Process Workflow/
├── Flowcharts/              # Mermaid diagram files
│   ├── Process flow.mmd     # Main process flowchart (8 phases)
│   ├── quadrantChart.mmd    # Example quadrant chart
│   └── sankey.mmd           # Example Sankey diagram
├── Lists/                   # JSON data files for AI tracking
│   ├── AI_Tool_Library.json # 73 AI tools catalog
│   ├── AI_Project_Portfolio.json
│   ├── AI_Strategic_Initiatives.json
│   └── Org_Structure.json   # Organizational hierarchy
├── Forms/                   # Assessment and submission templates
│   └── AI Risk Assessment Form
├── scripts/                 # Python utility scripts
│   ├── enrich_tool_data.py  # Web scraping for tool metadata
│   ├── fix_urls.py          # URL cleanup utilities
│   ├── migrate_tools.py     # CSV to JSON migration
│   └── parse_csv.py         # CSV data extraction
├── docs/                    # Web documentation (static site)
│   ├── index.html
│   ├── css/
│   ├── js/
│   └── data/
├── .github/                 # Repository configuration
│   ├── AGENTS.md            # AI agent instructions
│   ├── CONTRIBUTING.md      # Contributor guidelines
│   └── copilot-instructions.md
├── archive/                 # Archived/superseded files
├── build-site.ps1           # Static site build script
├── TODO.md                  # Task tracking
└── README.md                # This file
```

## 📂 Directory Navigation

| Folder | Purpose | Link |
|--------|---------|------|
| **Flowcharts/** | Mermaid process diagrams and journey maps | [View →](Flowcharts/README.md) |
| **Lists/** | JSON data files (tools, projects, initiatives) | [View →](Lists/README.md) |
| **Forms/** | Assessment templates and forms | [View →](Forms/README.md) |
| **scripts/** | Python utilities for data migration and enrichment | [View →](scripts/README.md) |
| **docs/** | Static website documentation | [View →](docs/) |
| **.github/** | Repository configuration and agent instructions | [View →](.github/README.md) |
| **archive/** | Superseded and archived files | [View →](archive/README.md) |

## 📊 Main Files

### Flowcharts & Diagrams

| File | Description | Type |
|------|-------------|------|
| [Process flow.mmd](Flowcharts/Process%20flow.mmd) | Complete AI software request lifecycle (8 phases: 0-7) | Flowchart |
| [quadrantChart.mmd](Flowcharts/quadrantChart.mmd) | Example: Campaign reach/engagement analysis | Quadrant Chart |
| [sankey.mmd](Flowcharts/sankey.mmd) | Example: Flow visualization | Sankey Diagram |

### Data Files

| File | Description | Items |
|------|-------------|-------|
| [AI_Tool_Library.json](Lists/AI_Tool_Library.json) | Catalog of AI tools and applications | 73 tools |
| [AI_Project_Portfolio.json](Lists/AI_Project_Portfolio.json) | Tracking all AI projects and experiments | 20 projects |
| [AI_Strategic_Initiatives.json](Lists/AI_Strategic_Initiatives.json) | C-level sponsored strategic AI programs | 3 initiatives |
| [Org_Structure.json](Lists/Org_Structure.json) | Organizational hierarchy for business groups | 8 groups |

### Forms & Templates

| File | Description | Use |
|------|-------------|-----|
| [Forms/AI Risk Assessment Form](Forms/AI%20Risk%20Assessment%20Form) | Risk evaluation template for AI systems | Required for all projects |

## 🔄 Process Flow Overview

The main process flow consists of **7 phases**:

1. **0. Required Inputs** - Initial documentation and prerequisites
2. **1.0 Request Phase** - Request submission and initial IT/Security review
3. **2.0 Interest Phase** - AI Board review and multi-business interest evaluation
4. **3.0 Demo Phase** - Vendor demonstration and stakeholder approval
5. **4.0 Pilot Phase** - Success criteria definition and pilot execution
6. **5.0 Formal Request** - Business case development and leadership approval
7. **6.0 Implementation** - Architecture review, procurement, and deployment
8. **7.0 Continuous Evaluation** - Ongoing success criteria monitoring

## 🛠️ Viewing the Diagrams

### VS Code
- Install the [Mermaid Preview](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid) extension
- Open any `.mmd` file and use the preview pane

### GitHub
- GitHub natively renders Mermaid diagrams in markdown files
- Wrap the content in ` ```mermaid ` code blocks

### Online Tools
- [Mermaid Live Editor](https://mermaid.live/)
- Copy and paste the diagram code to visualize and edit

## � Directory Details

### [Lists/](Lists/)
JSON data files replacing SharePoint lists. Contains:
- Tool library with vendor, status, and licensing info
- Project portfolio tracking 20 active initiatives
- Strategic initiatives with executive sponsorship

See [Lists/README.md](Lists/README.md) for schema details and usage examples.

### [Forms/](Forms/)
Assessment templates and submission forms. Contains:
- AI Risk Assessment Form (JSON template)
- Required for pilot phase approval

See [Forms/README.md](Forms/README.md) for completion guidelines.

### [Flowcharts/](Flowcharts/)
Reserved for additional process diagrams. Main flowcharts currently in root.

See [Flowcharts/README.md](Flowcharts/README.md) for diagram conventions.

### [.github/](.github/)
GitHub configuration and maintenance documentation:
- `AGENTS.md` - Comprehensive AI agent instructions
- `CONTRIBUTING.md` - Human contributor guidelines
- `copilot-instructions.md` - Quick reference for AI assistants

See [.github/README.md](.github/README.md) for workflow details.

## 📖 Documentation

### For AI Agents
- [.github/AGENTS.md](.github/AGENTS.md) - **Primary reference** for maintaining diagrams
- [.github/copilot-instructions.md](.github/copilot-instructions.md) - Quick reference guide

### For Human Contributors
- [.github/CONTRIBUTING.md](.github/CONTRIBUTING.md) - Contribution workflow and guidelines
- [TODO.md](TODO.md) - Current tasks and project status

## 🎨 Styling Guide

Each phase uses consistent color coding:
- **Inputs**: `#4A90E2` (Blue)
- **Request**: `#7B4397` (Purple)
- **Interest**: `#1B9B8E` (Teal)
- **Demo**: `#00A0E9` (Light Blue)
- **Pilot**: `#D4A017` (Gold)
- **Formal**: `#945491` (Magenta)
- **Implementation**: `#1E3A5F` (Dark Blue)
- **Evaluation**: `#7CB342` (Green)
- **Exit/Notification**: `#FF7F7F` (Red)

## 📝 Contributing

1. Follow the sequence numbering convention (Phase.Step format, e.g., `1.1`, `1.2`)
2. Maintain color consistency per phase
3. Validate all external links
4. Update cross-references in related diagrams when making changes

## 🔗 Quick Links

| Resource | Purpose |
|----------|---------|
| [Flowcharts/Process flow.mmd](Flowcharts/Process%20flow.mmd) | View main process flowchart |
| [Lists/AI_Tool_Library.json](Lists/AI_Tool_Library.json) | Browse 73 AI tools catalog |
| [Lists/AI_Project_Portfolio.json](Lists/AI_Project_Portfolio.json) | See all active AI projects |
| [Forms/AI Risk Assessment Form](Forms/AI%20Risk%20Assessment%20Form) | Download risk assessment template |
| [.github/AGENTS.md](.github/AGENTS.md) | Diagram maintenance instructions |
| [TODO.md](TODO.md) | Current tasks and backlog |

## 📞 Support

- **Process Questions**: AI Governance Committee
- **Technical Issues**: IT Shared Services
- **Risk Assessments**: AI Governance Committee
- **Repository Maintenance**: GitHub repository administrators

---

*Last Updated: January 16, 2026 | Version 2.0*
