# Scripts - Python Utilities

This directory contains Python utility scripts for data migration, enrichment, and maintenance of the AI Tool Library.

## Purpose

Automated scripts for:
- **Data migration** - Converting CSV data to JSON format
- **Web enrichment** - Fetching tool descriptions and metadata
- **Data cleanup** - Normalizing and updating field structures
- **URL fixing** - Decoding redirect URLs from web searches

## 📋 Contents

| Script | Purpose | Usage |
|--------|---------|-------|
| [enrich_tool_data.py](enrich_tool_data.py) | Web scraping to populate missing tool data (URL, description, vendor) | `python enrich_tool_data.py` |
| [fix_urls.py](fix_urls.py) | Decode DuckDuckGo redirect URLs to clean URLs | `python fix_urls.py` |
| [migrate_tools.py](migrate_tools.py) | Migrate AI Platform tools from CSV to AI_Tool_Library.json | `python migrate_tools.py` |
| [parse_csv.py](parse_csv.py) | Extract AI Platform entries from SharePoint CSV export | `python parse_csv.py` |
| [cleanup_legacy_data.py](cleanup_legacy_data.py) | Remove obsolete legacy fields from tool records | `python cleanup_legacy_data.py` |
| [update_tool_fields.py](update_tool_fields.py) | Add/remove fields in tool library schema | `python update_tool_fields.py` |
| [export_tools_to_csv.py](export_tools_to_csv.py) | Export AI_Tool_Library.json to timestamped CSV file | `python export_tools_to_csv.py` |
| [export_to_csv.py](export_to_csv.py) | **Sync all JSON files to CSV** (Tools, Projects, Initiatives) - **Used by RUN CLEANUP** | `python export_to_csv.py` |
| [ai_platforms_extracted.json](ai_platforms_extracted.json) | Intermediate data file (73 AI Platform entries) | - |

## 🛠️ Tech Stack

- **Python 3.14** - Runtime environment
- **requests** - HTTP library for web scraping
- **beautifulsoup4** - HTML parsing for web data extraction
- **json** - Data serialization and storage
- **csv** - CSV file parsing

## 🚀 Setup

### Prerequisites

1. Python 3.14 or higher
2. Virtual environment (recommended)

### Installation

```bash
# Create virtual environment (from repository root)
python -m venv .venv

# Activate virtual environment
# Windows PowerShell:
.venv\Scripts\Activate.ps1

# Install dependencies
pip install requests beautifulsoup4
```

## 📖 Script Details

### enrich_tool_data.py

**Purpose**: Web scraping to populate missing tool metadata

**Features**:
- Searches DuckDuckGo for tool information
- Extracts tool descriptions from web pages
- Identifies vendor names
- Decodes redirect URLs
- Interactive mode with confirmation prompts

**Usage**:
```bash
cd scripts
python enrich_tool_data.py
```

**Output**: Updates `../Lists/AI_Tool_Library.json` with enriched data

---

### fix_urls.py

**Purpose**: Clean up DuckDuckGo redirect URLs

**Features**:
- Parses `//duckduckgo.com/l/?uddg=` redirect URLs
- Extracts clean destination URLs
- Updates tool library in place

**Usage**:
```bash
cd scripts
python fix_urls.py
```

**Output**: Fixed 71 URLs in AI_Tool_Library.json

---

### migrate_tools.py

**Purpose**: Migrate AI Platform projects from CSV to JSON

**Features**:
- Reads from `ai_platforms_extracted.json`
- Maps CSV fields to tool library schema
- Generates unique tool IDs (TL###)
- Preserves legacy data for reference

**Usage**:
```bash
cd scripts
python migrate_tools.py
```

**Input**: `ai_platforms_extracted.json`
**Output**: Updates `../Lists/AI_Tool_Library.json`

---

### export_tools_to_csv.py

**Purpose**: Export tool library to CSV format for regular updates

**Features**:
- Exports all 73 tools to timestamped CSV file
- Flattens nested legacyData fields
- Includes all 16 fields from tool schema
- Generates filename: `AI_Tool_Library_YYYY-MM-DD.csv`

**Usage**:
```bash
cd scripts
python export_tools_to_csv.py
```

**Output**: `../Lists/AI_Tool_Library_2026-01-16.csv` (16 columns, 73 rows)

---

### export_to_csv.py

**Purpose**: Sync all JSON data files to CSV format (used by RUN CLEANUP)

**Features**:
- Exports all 3 data files to matching CSV names (no timestamps)
- AI_Tool_Library.json → AI_Tool_Library.csv (73 tools, 16 columns)
- AI_Project_Portfolio.json → AI_Project_Portfolio.csv (19 projects, 19 columns)
- AI_Strategic_Initiatives.json → AI_Strategic_Initiatives.csv (7 initiatives, 18 columns)
- Automatically called during RUN CLEANUP workflow

**Usage**:
```bash
cd scripts
python export_to_csv.py
```

**Output**: 
- `../Lists/AI_Tool_Library.csv`
- `../Lists/AI_Project_Portfolio.csv`
- `../Lists/AI_Strategic_Initiatives.csv`

---

### parse_csv.py

**Purpose**: Extract AI Platform entries from SharePoint export

**Features**:
- Filters for "01 - AI Platform" type solutions
- Skips CSV schema header row
- Preserves all original field data

**Usage**:
```bash
cd scripts
python parse_csv.py
```

**Input**: `../archive/Enterprise_AI_Project_Activity.csv`
**Output**: `ai_platforms_extracted.json`

---

### cleanup_legacy_data.py

**Purpose**: Remove obsolete fields from legacy data

**Features**:
- Retains only `activityStage` and `pipelineStatus`
- Removes `enterpriseScaleable`, `leadActivityBU`, `tdyBU`, `tdyGroup`
- Updates all 73 tools

**Usage**:
```bash
cd scripts
python cleanup_legacy_data.py
```

---

### update_tool_fields.py

**Purpose**: Schema migration for tool library

**Features**:
- Adds: `RiskAssessmentSubmitted`, `BusinessOwner`, `ToolURL`, `ToolImageURL`
- Removes: `licenseCount`, `annualCost`, `launchDate`, `documentationLink`
- Maintains field ordering

**Usage**:
```bash
cd scripts
python update_tool_fields.py
```

## ⚠️ Important Notes

1. **Always run scripts from the scripts/ directory** - File paths are relative to `scripts/`
2. **Backup data before running** - Scripts modify `Lists/AI_Tool_Library.json` directly
3. **Virtual environment** - Recommended to avoid package conflicts
4. **Rate limiting** - `enrich_tool_data.py` includes delays to avoid overwhelming web servers

## 🔄 Typical Workflow

For migrating new CSV data:

```bash
cd scripts

# 1. Extract AI Platform entries
python parse_csv.py

# 2. Migrate to tool library
python migrate_tools.py

# 3. Enrich with web data
python enrich_tool_data.py

# 4. Fix any redirect URLs
python fix_urls.py

# 5. Clean up legacy fields
python cleanup_legacy_data.py
```

## Navigation

- [← Back to Root](../README.md)
- [Lists](../Lists/README.md) - Target data files
- [archive](../archive/README.md) - Source CSV files
- [.github](../.github/README.md) - Repository configuration

---

*These scripts are archived for reference and may require updates if the data schema changes.*
