API_KEY = "e784641eb314460fa18b8cdc8146be57"
HEADERS = {
    'x-api-key': API_KEY
}
FONT = ('Helvetica', 36, "normal")


def format_instructions(instructions_data):
    formatted_text = ""
    for section in instructions_data:
        formatted_text += f"{section['name']}:\n"
        for step in section['steps']:
            formatted_text += f"{step['number']}. {step['step']}\n"
            if 'ingredients' in step:
                formatted_text += "   - Ingredients: " + ", ".join(
                    ingredient['name'] for ingredient in step['ingredients']) + "\n"
            if 'equipment' in step:
                equipment_list = [equipment['name'] for equipment in step['equipment']]
                if equipment_list:
                    formatted_text += "   - Equipment: " + ", ".join(equipment_list) + "\n"
            if 'length' in step:
                formatted_text += f"   - Time: {step['length']['number']} {step['length']['unit']}\n"
        formatted_text += "\n"

    return formatted_text
