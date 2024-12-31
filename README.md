# Clear The Clutter 🧹

A simple Python tool to **organize and rename your files** — quickly clean up those messy filenames and make them easier to manage. 🚀

## ✨ Features

- **Remove Unwanted Characters**: Clean up filenames by removing special symbols, spaces, and other unwanted characters.
- **Rename Sequentially**: Automatically rename files in a logical, sequential order (e.g., `File_1`, `File_2`, etc.).
- **Move Files**: After renaming, files are neatly moved to a designated folder.

## ⚙️ How It Works

1. **Place your files** in the source folder (e.g., `Pictures`).
2. **Run the script** to:
   - Rename files sequentially.
   - Remove unwanted characters.
   - Move the files to a clean, organized folder.

### 🔧 Customizing

To change the folder locations:

- Modify the `folderPath` for your source folder (where the unorganized files are).
- Set the `renamePath` to the destination folder (where you want your files to go after renaming).

```python
folderPath = "/path/to/source/folder"
renamePath = "/path/to/destination/folder"
```

## 🏃‍♂️ Running the Script

1. Install any required dependencies (if necessary).
2. Run the Python script:

   ```bash
   python main.py
   ```

3. Your files will be renamed and neatly moved to the `renamePath` folder.

## 🧑‍💻 Example

```bash
Pictures/
  ├── img_1.jpg
  ├── pic#2.jpg
  └── photo_03!.png

# After running the script:
renamedFiles/
  ├── File_1.jpg
  ├── File_2.jpg
  └── File_3.png
```

## 🎯 Why You Need This

- **Save Time:** Quickly organize large collections of files without manual renaming.
- **Keep It Clean:** Clear filenames mean easier navigation, better searchability, and fewer errors.
- **Effortless Organization:** Move and rename files without the hassle.

## 💡 Future Ideas

- Support for other file formats (audio, videos, etc.)
- Option for custom naming patterns
- Ability to undo renames or batch processing options

## 🧑‍🤝‍🧑 Contributing

Feel free to submit issues, bugs, or pull requests! Let's make this tool even better. 🚀
