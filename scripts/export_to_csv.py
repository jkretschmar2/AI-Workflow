import json
import csv
from pathlib import Path

def export_tool_library():
    """Export AI_Tool_Library.json to CSV"""
    
    with open('../Lists/AI_Tool_Library.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    tools = data.get('tools', [])
    
    fieldnames = [
        'toolId', 'oldSharePointId', 'toolName', 'category', 'typeOfSolution',
        'status', 'vendor', 'descriptionOfTool', 'descriptionOfUse',
        'championOwner', 'RiskAssessmentSubmitted', 'BusinessOwner',
        'ToolURL', 'ToolImageURL', 'legacyData_activityStage', 'legacyData_pipelineStatus'
    ]
    
    output_file = '../Lists/AI_Tool_Library.csv'
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for tool in tools:
            row = {
                'toolId': tool.get('toolId', ''),
                'oldSharePointId': tool.get('oldSharePointId', ''),
                'toolName': tool.get('toolName', ''),
                'category': tool.get('category', ''),
                'typeOfSolution': tool.get('typeOfSolution', ''),
                'status': tool.get('status', ''),
                'vendor': tool.get('vendor', ''),
                'descriptionOfTool': tool.get('descriptionOfTool', ''),
                'descriptionOfUse': tool.get('descriptionOfUse', ''),
                'championOwner': tool.get('championOwner', ''),
                'RiskAssessmentSubmitted': tool.get('RiskAssessmentSubmitted', ''),
                'BusinessOwner': tool.get('BusinessOwner', ''),
                'ToolURL': tool.get('ToolURL', ''),
                'ToolImageURL': tool.get('ToolImageURL', ''),
                'legacyData_activityStage': tool.get('legacyData', {}).get('activityStage', ''),
                'legacyData_pipelineStatus': tool.get('legacyData', {}).get('pipelineStatus', '')
            }
            writer.writerow(row)
    
    print(f"✓ AI_Tool_Library.csv: {len(tools)} tools")
    return len(tools)

def export_project_portfolio():
    """Export AI_Project_Portfolio.json to CSV"""
    
    with open('../Lists/AI_Project_Portfolio.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    projects = data.get('projects', [])
    
    fieldnames = [
        'projectId', 'oldSharePointId', 'projectName', 'businessSegment',
        'projectType', 'status', 'stage', 'description', 'businessObjective',
        'projectOwner', 'technicalLead', 'startDate', 'targetCompletionDate',
        'budgetAllocated', 'resourcesRequired', 'keyMilestones',
        'successMetrics', 'riskLevel', 'dependencies', 'notes'
    ]
    
    output_file = '../Lists/AI_Project_Portfolio.csv'
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for project in projects:
            row = {field: project.get(field, '') for field in fieldnames}
            writer.writerow(row)
    
    print(f"✓ AI_Project_Portfolio.csv: {len(projects)} projects")
    return len(projects)

def export_strategic_initiatives():
    """Export AI_Strategic_Initiatives.json to CSV"""
    
    with open('../Lists/AI_Strategic_Initiatives.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    initiatives = data.get('initiatives', [])
    
    fieldnames = [
        'initiativeId', 'oldSharePointId', 'initiativeName', 'executiveSponsor',
        'strategicObjective', 'description', 'businessValue', 'status',
        'startDate', 'targetCompletionDate', 'totalInvestment', 'resourcesAllocated',
        'keyMilestones', 'successMetrics', 'riskLevel', 'complianceRequirements',
        'relatedProjects', 'notes'
    ]
    
    output_file = '../Lists/AI_Strategic_Initiatives.csv'
    
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for initiative in initiatives:
            row = {field: initiative.get(field, '') for field in fieldnames}
            writer.writerow(row)
    
    print(f"✓ AI_Strategic_Initiatives.csv: {len(initiatives)} initiatives")
    return len(initiatives)

def export_all():
    """Export all JSON files to CSV"""
    print("Exporting JSON data to CSV files...\n")
    
    try:
        tool_count = export_tool_library()
        project_count = export_project_portfolio()
        initiative_count = export_strategic_initiatives()
        
        print(f"\n✓ Export complete:")
        print(f"  - {tool_count} tools")
        print(f"  - {project_count} projects")
        print(f"  - {initiative_count} initiatives")
        
        return True
    except Exception as e:
        print(f"✗ Error during export: {e}")
        return False

if __name__ == "__main__":
    export_all()
