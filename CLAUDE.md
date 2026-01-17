# CLAUDE.md - AI Assistant Guidelines

This document provides guidance for AI assistants (Claude, Copilot, etc.) working with the AI Process Workflow repository.

## Project Overview

**Purpose**: Document and standardize the AI Software Request governance process workflow at Teledyne. This repository provides visual process flows, data tracking, and assessment templates for consistent evaluation and approval of AI tools and projects.

**Target Audience**:
- AI Governance Committee members
- Business unit leaders requesting AI tools
- IT and Security teams
- Developers maintaining process documentation

**Current Status**: Early-stage documentation project with planning artifacts. Most implementation files are planned but not yet created.

## Repository Structure

```
AI-Workflow/
├── Flowcharts/              # Mermaid diagram files (.mmd)
│   ├── Process flow.mmd     # Main 8-phase process flowchart
│   ├── quadrantChart.mmd    # Risk/Value analysis visualization
│   └── sankey.mmd           # Flow visualization
├── Lists/                   # JSON data files
│   ├── AI_Tool_Library.json # Catalog of AI tools (73 tools)
│   ├── AI_Project_Portfolio.json # Active AI projects (20)
│   ├── AI_Strategic_Initiatives.json # C-level initiatives (3)
│   └── Org_Structure.json   # Organizational hierarchy (8 groups)
├── Forms/                   # Assessment templates
│   └── AI Risk Assessment Form
├── scripts/                 # Python utility scripts
│   ├── enrich_tool_data.py  # Web scraping for tool metadata
│   ├── fix_urls.py          # URL cleanup utilities
│   ├── migrate_tools.py     # CSV to JSON migration
│   └── parse_csv.py         # CSV data extraction
├── docs/                    # Static website
│   ├── index.html
│   ├── css/
│   ├── js/
│   └── data/                # Build output (copied JSON/mmd files)
├── .github/                 # Repository configuration
│   ├── AGENTS.md            # AI agent instructions
│   ├── CONTRIBUTING.md      # Contributor guidelines
│   └── copilot-instructions.md
├── archive/                 # Superseded files
├── build-site.ps1           # PowerShell build script
├── README.md                # Project documentation
├── TODO.md                  # Task tracking and roadmap
├── directory.md             # Structure reference
└── CLAUDE.md                # This file
```

## Technology Stack

| Technology | Purpose |
|------------|---------|
| **Mermaid** | Diagram-as-code (flowcharts, journey maps, quadrant charts, sankey diagrams) |
| **JSON** | Data storage for tools, projects, and initiatives |
| **Markdown** | Documentation format |
| **HTML/CSS/JS** | Static site in `docs/` folder |
| **PowerShell** | Build automation (`build-site.ps1`) |
| **Python** | Utility scripts for data processing |
| **Git/GitHub** | Version control |

## Key Files

### Documentation
- `README.md` - Main project guide with table of contents and quick links
- `TODO.md` - Task backlog organized by priority categories
- `directory.md` - Quick structure reference

### Build System
- `build-site.ps1` - Copies JSON files from `Lists/` and Mermaid files from `Flowcharts/` to `docs/data/`

### Data Files (in `Lists/`)
| File | Description | Schema Notes |
|------|-------------|--------------|
| `AI_Tool_Library.json` | AI tools catalog | Fields: Orig ID, Tool Name, Category, Vendor, Status, Licensing |
| `AI_Project_Portfolio.json` | Active AI projects | 20 tracked projects |
| `AI_Strategic_Initiatives.json` | Executive-sponsored programs | 3 C-level initiatives |
| `Org_Structure.json` | Business unit hierarchy | 8 organizational groups |

## Process Flow (8 Phases)

The core governance workflow consists of 8 phases:

| Phase | Name | Color | Hex Code |
|-------|------|-------|----------|
| 0 | Required Inputs | Blue | `#4A90E2` |
| 1 | Request | Purple | `#7B4397` |
| 2 | Interest | Teal | `#1B9B8E` |
| 3 | Demo | Light Blue | `#00A0E9` |
| 4 | Pilot | Gold | `#D4A017` |
| 5 | Formal Request | Magenta | `#945491` |
| 6 | Implementation | Dark Blue | `#1E3A5F` |
| 7 | Continuous Evaluation | Green | `#7CB342` |
| Exit | Exit/Notification | Red | `#FF7F7F` |

## Conventions and Guidelines

### Naming Conventions
- **Sequence numbering**: Use `Phase.Step` format (e.g., `1.1`, `1.2`, `2.1`)
- **Mermaid files**: Use `.mmd` extension
- **JSON data files**: Use `PascalCase_With_Underscores.json`
- **Documentation**: Use Markdown with descriptive filenames

### Mermaid Diagram Guidelines
1. Maintain consistent color coding per phase (see table above)
2. Use standard shapes for different node types
3. Validate all external links in diagrams
4. Update cross-references when making changes
5. Keep sequence numbering continuous within phases

### JSON Data Guidelines
1. Validate against schema before committing
2. Maintain data type consistency (Number, Text, Dropdown, Currency)
3. Enforce field constraints as documented
4. Mark required fields appropriately

### Code Style
- **PowerShell**: Use `Write-Host` for build output messages
- **Python**: Follow PEP 8 conventions
- **Markdown**: Use GitHub-flavored markdown

## Development Workflow

### Building the Static Site
```powershell
# From repository root
.\build-site.ps1
```
This copies:
- `Lists/*.json` → `docs/data/`
- `Flowcharts/*.mmd` → `docs/data/`

### Viewing Mermaid Diagrams
1. **VS Code**: Install the "Mermaid Preview" extension
2. **GitHub**: Wrap content in ` ```mermaid ` code blocks
3. **Online**: Use [Mermaid Live Editor](https://mermaid.live/)

### Making Changes
1. Read `TODO.md` for current priorities and backlog
2. Follow the sequence numbering convention
3. Maintain color consistency per phase
4. Update related documentation when modifying diagrams
5. Run `build-site.ps1` after changing `Lists/` or `Flowcharts/`

## Important Directories

| Directory | Purpose | When to Modify |
|-----------|---------|----------------|
| `Flowcharts/` | Mermaid diagram source files | When updating process flows |
| `Lists/` | JSON data source files | When updating tool/project data |
| `docs/` | Static site output | Via build script only |
| `scripts/` | Python utilities | When adding data processing |
| `Forms/` | Assessment templates | When updating form fields |
| `.github/` | Repo config and AI instructions | When updating contribution guidelines |
| `archive/` | Deprecated files | When archiving old content |

## Current Priorities (from TODO.md)

1. **HIGH - Diagram Enhancements**: High-level governance flowchart, scoring visualizations, pipeline flows
2. **HIGH - Web Development**: Update `docs/` site, add interactive filtering
3. **HIGH - Microsoft 365 Integration**: SharePoint forms, Power Automate workflows
4. **HIGH - Governance Artifacts**: RACI matrices, org structure documentation
5. **MEDIUM - Workstream Blueprints**: Tool evaluation, project lifecycle, compliance workflows
6. **MEDIUM - Reporting**: Power BI dashboards, KPI framework

## Standards and Compliance

This project references:
- **ISO 31000** - Risk Management
- **ISO/IEC 27001** - Information Security
- **ISO/IEC 42001** - AI Management Systems

## Quick Reference Commands

```bash
# View repository structure
ls -la

# Build static site (PowerShell)
pwsh build-site.ps1

# Run Python scripts
python scripts/enrich_tool_data.py
python scripts/fix_urls.py
python scripts/migrate_tools.py
python scripts/parse_csv.py
```

## What NOT to Do

1. **Don't modify `docs/data/` directly** - Use `Lists/` and `Flowcharts/` source files
2. **Don't break sequence numbering** - Maintain continuous Phase.Step format
3. **Don't use inconsistent colors** - Follow the phase color palette
4. **Don't commit without validation** - Check JSON schema and link integrity
5. **Don't remove files without archiving** - Move deprecated files to `archive/`

## Related Documentation

- [README.md](README.md) - Full project documentation
- [TODO.md](TODO.md) - Task backlog and roadmap
- [.github/AGENTS.md](.github/AGENTS.md) - Detailed AI agent instructions
- [.github/CONTRIBUTING.md](.github/CONTRIBUTING.md) - Human contributor guidelines

## Contact

- **Process Questions**: AI Governance Committee
- **Technical Issues**: IT Shared Services
- **Risk Assessments**: AI Governance Committee
- **Repository Maintenance**: GitHub repository administrators

---

*Last Updated: January 17, 2026*
