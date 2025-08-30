# This is a task program fully written in [cbLang](https://github.com/Ceebox/cbLang)
by [Tamino1230](https://github.com/Tamino1230/)

## Setup Download
Run `setup.py` and run it with admin and then enter `add` to install the language. By downloading it like this you can just doubleclick the main.cb file.
Write `remove` to uninstall the file. The download path is: `C:\\Program Files\\cbLang`. The Setup will download everything automaticly!

---

To run the program you need the cbLang "interpreter" here is a [cbLang interpreter direct download](https://github.com/Ceebox/cbLang/releases/download/0.1.2/cbLang.exe)

Then just run the program with `cblang.exe --run main.cb` (exe has to be in the same folder as `main.cb`) or if you put it in your environment path variable use `cblang --run main.cb`

Because i wasnt able to use dictionaries i couldnt use json files to save but a txt file will do it too. This is a example for the cbLang Language, i got familiar with it. But it still has some bugs.
Update: I could make a dict with to make it saving in json:
```
my_dict = dict(a=1, b=2, c=3)
print(my_dict) # {'a': 1, 'b': 2, 'c': 3}
```

Especially TRY and EXCEPT was kinda tricky because the programming language doesnt just let me do:
```
try {
    new = int(old_str);
} except {
    pass;
}
```

because the following error will accure `Missing semicolon in: try {` and i couldnt make it work in a single line, because then it will say: `Braces amount is not equal`.
Update: I could make an try/except with:
```
from contextlib import suppress

s = "abc"
with suppress(ValueError):
    x = int(s)
```
```
// or in cbLang
from native reference contextlib;

s = "abc"
with contextlib.supress(ValueError):
    x = int(s)
```

So except of try i used this:
```
// first check if is a number
if not (index.isdigit())
{
    print("Invalid task ID");
    return;
}

// if yes convert to int
index = int(index);

// check if index is valid
task_len = len(this.tasks);
if (index < 1 or index > task_len)
{
    print("Invalid task ID");
    return;
}

// then pop out of list etc.
```

#### [cbLang by github.com/Ceebox/](https://github.com/Ceebox/)
