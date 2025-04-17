def read_and_modify_file():
    try:
        # 🧪 Ask the user for the input filename
        input_filename = input("Enter the name of the file to read from: ")

        # 📖 Try to open and read the input file
        with open(input_filename, 'r') as infile:
            content = infile.read()
            print("✅ File read successfully!")

        # ✍️ Modify the content (e.g., make it uppercase)
        modified_content = content.upper()

        # 🖋️ Create a new filename for the modified content
        output_filename = "modified_" + input_filename

        # 📄 Write the modified content to the new file
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
            print(f"✅ Modified content written to '{output_filename}'")

    except FileNotFoundError:
        print("❌ Error: The file was not found.")
    except IOError:
        print("❌ Error: The file could not be read or written.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# 🔁 Run the function
read_and_modify_file()
