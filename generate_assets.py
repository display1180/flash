import os
import json

def main():
    asset_dir = 'asset'
    output_file = 'assets.json'
    
    if not os.path.exists(asset_dir):
        print(f"Directory {asset_dir} not found.")
        return
        
    valid_extensions = {'.mp4', '.mov', '.webm'}
    asset_list = []
    
    for filename in os.listdir(asset_dir):
        if any(filename.lower().endswith(ext) for ext in valid_extensions):
            asset_list.append({
                'id': filename,
                'type': 'local',
                'src': f"{asset_dir}/{filename}",
                'label': filename[:30] + '...' if len(filename) > 30 else filename
            })
            
    # Sort alphabetically
    asset_list.sort(key=lambda x: x['label'])
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(asset_list, f, ensure_ascii=False, indent=2)
        
    print(f"Successfully generated {output_file} with {len(asset_list)} items.")

if __name__ == '__main__':
    main()
