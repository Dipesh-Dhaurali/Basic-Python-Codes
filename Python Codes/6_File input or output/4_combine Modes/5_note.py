"""
cont...(26:30)
"""


"""
r+ = read and overwrite , pointer is in starting   ,to read file need seek method => (no truncate)


w+ = read and overwrite , file is empty cause      ,to read file need seek method => (truncate)
                          remove all string so 
                          pointer is in staring
                          
a+ = read and append    , pointer is in end        ,to read file need seek method =>(no truncate) 

"""




"""
Mode | Description | File Pointer Position | File Exists | File Truncated? | Reading Allowed | Writing Behavior
r+ | Read and write | Start of file | ✅ Required | ❌ No | ✅ Yes | Overwrites from the beginning
w+ | Write and read (overwrite) | Start of file | ✅/❌ Optional | ✅ Yes | ✅ Yes (after seek) | File is cleared first
a+ | Append and read | End of file | ✅/❌ Optional | ❌ No | ✅ Yes (after seek) | Appends at the end only

"""