# ZIP a sequence of files in Lua (Linux/Windows)

**This Lua script provides functions to compress the contents of a folder into a ZIP file. It supports both Windows and Unix-based systems (Linux and macOS).**

## Functions

### 1. file_exists(file_path)

This function checks if a file exists at the given `file_path`.

- `file_path`: The path of the file to check for existence.

**Returns:** `true` if the file exists, `false` otherwise.

### 2. remove_file(file_path)

This function removes a file at the given `file_path`.

- `file_path`: The path of the file to remove.

### 3. compress_folder_to_zip(folder_path, zip_path)

This function compresses the content of the folder at `folder_path` into a ZIP file located at `zip_path`.

- `folder_path`: The path of the folder to compress.
- `zip_path`: The path where the ZIP file should be saved.

```lua
function file_exists(file_path)
  local file = io.open(file_path, "r")
  if file then
    file:close()
    return true
  else
    return false
  end
end

function remove_file(file_path)
  local command
  if package.config:sub(1,1) == '\\' then
    -- Windows system
    command = string.format('del /Q /F "%s"', file_path)
  else
    -- Unix-based system (Linux or macOS)
    command = string.format('rm -f "%s"', file_path)
  end

  os.execute(command)
end

function compress_folder_to_zip(folder_path, zip_path)
  if file_exists(zip_path) then
    remove_file(zip_path)
  end

  local command
  if package.config:sub(1,1) == '\\' then
    -- Windows system
    command = string.format('powershell -command "Compress-Archive -Path \'%s\\*\' -DestinationPath \'%s\'"', folder_path, zip_path)
  else
    -- Unix-based system (Linux or macOS)
    command = string.format('zip -r "%s" "%s"', zip_path, folder_path)
  end

  os.execute(command)
end

-- Usage example:
local folder_path = "/path/to/your/folder"
local zip_path = "/path/to/the/zip/file/output.zip"
compress_folder_to_zip(folder_path, zip_path)
```
