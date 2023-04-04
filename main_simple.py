from main_simple_lib import load_image, show_single_image, get_code, execute_code

im = load_image(
    "https://wondermamas.com/wp-content/uploads/2020/04/IMG_8950-min-1024x1024.jpg"
)
query = "How many muffins can each kid have for it to be fair?"

show_single_image(im)
code = get_code(query)

execute_code(code, im, show_intermediate_steps=True)
