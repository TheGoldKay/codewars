# Generate mod.rs with public module declarations for each .rs file
# run it with `bash setup.sh` inside the src directory

for file in solutions/*.rs; do
    if [ "$(basename "$file")" != "mod.rs" ]; then
        echo "pub mod $(basename "$file" .rs);" >> solutions/mod.rs
    fi
done