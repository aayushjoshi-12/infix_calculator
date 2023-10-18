page_style=dict(
    background_image="linear-gradient(90deg, rgba(223,231,6,1) 0%, rgba(255,136,0,1) 100%)",
    height="100vh",
    max_width="auto",
    position="relative",
    overlay="hidden",
    place_items="center",
)
head_style=dict(
    background="white",
    background_clip="text",
    font_weight="extrabold",
    font_size="3em",
    text_align="center",
    margin="1em",
    z_index="1"
)
glass_style=dict(
    background="rgba(255,255,255,0.2)",
    box_shadow="0 4px 30px rgba(0,0,0,0.1)",
    border="1px solid rgba(255,255,255,0.3)",
)
shape_style=dict(
    width="120px",
    height="120px",
    position="fixed",
    border_radius="50%",
    background_image="linear-gradient(39deg, rgba(6,126,231,1) 0%, rgba(0,255,238,1) 72%)",
    z_index="0",
    top="20%",
    left="40%",
)
base_style=glass_style | dict(
    height="400px",
    width="250px",
    border_radius="xl",
    padding="0.7em",
    z_index="3"
)
display_style=glass_style | dict(
    width="225px",
    height="40%",
    text_align="right",
    border_radius="xl",
    padding="0.5em",
    text_color="rgba(255,255,255,1)",
    z_index="3",
)
button_style=glass_style | dict(
    border_radius="10%",
    width="100%",
    text_align="centre",
    text_color="white",
    z_index="3",
)
keypad_style=dict(
    template_columns="repeat(4,1fr)",
    template_rows="repeat(5,1fr)",
    gap="0.2em",
    margin_y="0.7em",
    width="100%",
    z_index="3"
)
AC_button_style=button_style | dict(
    
)