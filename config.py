API_KEY = "e784641eb314460fa18b8cdc8146be57"
HEADERS = {
    'x-api-key': API_KEY
}
HEADER_FONT = ('Helvetica', 36, 'bold')
LABEL_FONT = ('Helvetica', 24, 'normal')
ENTRY_FONT = ('Helvetica', 20, 'normal')


def format_instructions(instructions_data):
    formatted_text = ""
    for section in instructions_data:
        formatted_text += f"{section['name']}:\n"
        for step in section['steps']:
            formatted_text += f"{step['number']}. {step['step']}\n"
            if 'ingredients' in step:
                formatted_text += "   - Ingredients: "
                ingredients_list = []
                for ingredient in step['ingredients']:
                    ingredient_str = ingredient['name']
                    if 'measurement' in ingredient:
                        measurement = ingredient['measurement']
                        ingredient_str += f" ({measurement['amount']} {measurement['unit']})"
                    ingredients_list.append(ingredient_str)
                formatted_text += ", ".join(
                    ingredients_list) + "\n"  # Displaying the ingredients along with measurements
            if 'equipment' in step:
                equipment_list = [equipment['name'] for equipment in step['equipment']]
                if equipment_list:
                    formatted_text += "   - Equipment: " + ", ".join(equipment_list) + "\n"
            if 'length' in step:
                formatted_text += f"   - Time: {step['length']['number']} {step['length']['unit']}\n"
        formatted_text += "\n"

    return formatted_text

