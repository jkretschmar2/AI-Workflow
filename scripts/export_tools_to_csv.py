import json
import csv
from datetime import datetime

def export_tools_to_csv():
    """Export AI Tool Library to CSV format"""
    
    # Load the tool library
    with open('../Lists/AI_Tool_Library.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    tools = data.get('tools', [])
    
    if not tools:
        print("No tools found in AI_Tool_Library.json")
        return
    
    # Define CSV columns (all fields from the tool schema)
    fieldnames = [
        'toolId',
        'oldSharePointId',
        'toolName',
        'category',
        'typeOfSolution',
        'status',
        'vendor',
        'descriptionOfTool',
        'descriptionOfUse',
        'championOwner',
        'RiskAssessmentSubmitted',
        'BusinessOwner',
        'ToolURL',
        'ToolImageURL',
        'legacyData_activityStage',
        'legacyData_pipelineStatus'
    ]
    
    # Generate output filename with timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d')
    output_file = f'../Lists/AI_Tool_Library_{timestamp}.csv'
    
    # Write to CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write header
        writer.writeheader()
        
        # Write data rows
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
    
    print(f"✓ Exported {len(tools)} tools to: {output_file}")
    print(f"  Columns: {len(fieldnames)}")
    return output_file

if __name__ == "__main__":
    export_tools_to_csv()
