import streamlit as st

# Set page title and favicon
st.set_page_config(page_title="My Landing Page", page_icon=":alpha:",
   initial_sidebar_state="expanded",)

# Add header text and logo
st.title("Welcome to My Landing Page!")
# st.image("logo.png")

# Add search box
search_query = st.text_input("Search for something")

# Add multiselect
options = [1, 2, 3, 4, 5]
selected_options = st.multiselect("Choose some options", options, default=[1, 2])

# Add random text paragraph
st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vel ante hendrerit, lobortis est eget, ultricies velit. Nam at dui vitae ipsum laoreet finibus. Donec id risus id augue tincidunt efficitur. Pellentesque euismod, dolor sit amet malesuada eleifend, augue mauris fringilla neque, vitae maximus lacus neque eget nisl. Donec id ex eget turpis blandit accumsan. Proin tempor eros quis tellus vestibulum, vitae lobortis augue aliquam. Nulla euismod tortor sed dolor cursus, vel ullamcorper massa gravida. Sed eget ornare turpis, quis aliquam nulla. Duis malesuada lectus vel ex malesuada rutrum.")
