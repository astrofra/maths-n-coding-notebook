# Lua Delete Files with Prefix

**This Lua script provides a function to delete files with a specific prefix in a given folder. It supports both Windows and Unix-based systems (Linux and macOS).**

## Function

### delete_files_with_prefix(folder_path, prefix)

This function deletes files with a specific `prefix` in the given `folder_path`.

- `folder_path`: The path of the folder containing the files to delete.
- `prefix`: The prefix of the filenames that should be deleted.

```lua
function delete_files_with_prefix(folder_path, prefix)
  local command
  if package.config:sub(1,1) == '\\' then
    -- Windows system
    command = string.format('del /Q /F "%s\\%s*"', folder_path, prefix)
  else
    -- Unix-based system (Linux or macOS)
    command = string.format('rm -f "%s"/%s*', folder_path, prefix)
  end

  os.execute(command)
end

-- Usage :
local folder_path = "/path/to/my/folder"
local prefix = "frame_"
delete_files_with_prefix(folder_path, prefix)
```
