# Generate mod.rs with public module declarations for each .rs file
echo "// filepath: src/solutions/mod.rs" > src/solutions/mod.rs
for file in solutions/*.rs; do
    if [ "$(basename "$file")" != "mod.rs" ]; then
        echo "pub mod $(basename "$file" .rs);" >> solutions/mod.rs
    fi
done