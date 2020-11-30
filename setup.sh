mkdir -p -/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = SPORT\n\
enableCORS = false\n\
\n\
" > -/.streamlit/config.toml