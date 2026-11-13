# Regex

Regular Expressions (**Regex**) are powerful tools for **pattern matching** and **text processing** in programming.

Author

Benedict Thekkel

## **1. Basics of Regex Syntax**

### **Common Regex Symbols**

| Symbol | Description | Example | Matches |
|----|----|----|----|
| `.` | Any single character except newline | `a.b` | `acb`, `a1b`, `a_b` |
| `^` | Start of string | `^hello` | Matches “hello world”, not “world hello” |
| `$` | End of string | `world$` | Matches “hello world”, not “world hello” |
| `*` | 0 or more repetitions | `ab*` | Matches `a`, `ab`, `abb`, `abbb` |
| `+` | 1 or more repetitions | `ab+` | Matches `ab`, `abb`, `abbb` but not `a` |
| `?` | 0 or 1 occurrence | `colou?r` | Matches `color` and `colour` |
| `{n}` | Exactly `n` repetitions | `a{3}` | Matches `aaa` |
| `{n,}` | At least `n` repetitions | `a{2,}` | Matches `aa`, `aaa`, `aaaa` |
| `{n,m}` | Between `n` and `m` repetitions | `a{2,4}` | Matches `aa`, `aaa`, `aaaa` |
| `[]` | Character set | `[abc]` | Matches `a`, `b`, or `c` |
| `[^ ]` | Negated character set | `[^abc]` | Matches any character except `a`, `b`, `c` |
| `\d` | Digit (0-9) | `\d+` | Matches `123`, `456` |
| `\D` | Non-digit | `\D+` | Matches `abc`, `hello` |
| `\w` | Word character (a-z, A-Z, 0-9, \_) | `\w+` | Matches `hello123` |
| `\W` | Non-word character | `\W+` | Matches `@#$%^` |
| `\s` | Whitespace | `\s+` | Matches spaces, tabs, newlines |
| `\S` | Non-whitespace | `\S+` | Matches `hello`, `world` |
| `\b` | Word boundary | `\bhello\b` | Matches “hello” in “hello world” but not “helloworld” |
| `\B` | Non-word boundary | `\Bhello\B` | Matches “hello” inside a word |

------------------------------------------------------------------------

## **2. Groups & Alternation**

### **Using Parentheses for Grouping**

- `()` groups patterns together.
- **Example:** `(hello|hi)` matches `"hello"` or `"hi"`.

``` python
import re
pattern = re.compile(r"(hello|hi) world")
print(bool(pattern.search("hi world")))  # True
```

### **Capturing Groups**

- Captures parts of a match for later use.
- **Example:** Extract date `(2024-02-17)`

``` python
match = re.search(r"(\d{4})-(\d{2})-(\d{2})", "Date: 2024-02-17")
if match:
    print(match.group(1))  # "2024"
    print(match.group(2))  # "02"
    print(match.group(3))  # "17"
```

### **Non-Capturing Groups `(?:...)`**

- Groups without storing matches.

``` python
re.search(r"(?:hello|hi) world", "hi world")  # Matches but not stored
```

### **Named Groups `(?P<name>...)`**

- Assign names to capture groups.

``` python
match = re.search(r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})", "2024-02-17")
print(match.group("year"))  # 2024
```

------------------------------------------------------------------------

## **3. Lookaheads & Lookbehinds**

Lookaheads and Lookbehinds match a pattern without consuming characters.

### **Positive Lookahead `(?=...)`**

- Ensures something **follows** a pattern.
- **Example:** Match `hello` only if it’s followed by `world`

``` python
re.search(r"hello(?= world)", "hello world")  # Matches
```

### **Negative Lookahead `(?!...)`**

- Ensures something does **not** follow.
- **Example:** Match `hello` but not `hello world`

``` python
re.search(r"hello(?! world)", "hello everyone")  # Matches
```

### **Positive Lookbehind `(?<=...)`**

- Ensures something **precedes** a pattern.
- **Example:** Match `world` only if preceded by `hello`

``` python
re.search(r"(?<=hello )world", "hello world")  # Matches
```

### **Negative Lookbehind `(?<!...)`**

- Ensures something does **not** precede.
- **Example:** Match `world` only if **not** preceded by `hello`

``` python
re.search(r"(?<!hello )world", "hi world")  # Matches
```

------------------------------------------------------------------------

## **4. Regex in Python (`re` Module)**

### **Finding All Matches (`findall`)**

``` python
import re
text = "My number is 123-456-7890 and yours is 987-654-3210."
pattern = r"\d{3}-\d{3}-\d{4}"
matches = re.findall(pattern, text)
print(matches)  # ['123-456-7890', '987-654-3210']
```

### **Replacing Text (`sub`)**

``` python
text = "I love Java, Java is great!"
print(re.sub(r"Java", "Python", text))  # "I love Python, Python is great!"
```

### **Splitting Strings (`split`)**

``` python
text = "apple,banana;orange|grape"
print(re.split(r"[,;|]", text))  # ['apple', 'banana', 'orange', 'grape']
```

### **Case-Insensitive Search**

``` python
re.search(r"hello", "HELLO", re.IGNORECASE)  # Matches
```

------------------------------------------------------------------------

## **5. Practical Use Cases**

### **1️⃣ Validate Email Addresses**

``` python
email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
print(bool(re.match(email_pattern, "user@example.com")))  # True
```

### **2️⃣ Validate Phone Numbers**

``` python
phone_pattern = r"^\+?[1-9]\d{1,14}$"
print(bool(re.match(phone_pattern, "+1234567890")))  # True
```

### **3️⃣ Extract Hashtags from Text**

``` python
text = "Loving the #Python and #AI community!"
hashtags = re.findall(r"#\w+", text)
print(hashtags)  # ['#Python', '#AI']
```

### **4️⃣ Validate Password Strength**

``` python
password_pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
print(bool(re.match(password_pattern, "StrongP@ss1")))  # True
```

------------------------------------------------------------------------

## **6. Regex Performance Optimization**

- Use **raw strings (`r"pattern"`)** to avoid escaping issues.

- Use **compiled regex** when reusing patterns:

  ``` python
  pattern = re.compile(r"\d{3}-\d{3}-\d{4}")
  pattern.findall("Call 123-456-7890 or 987-654-3210")
  ```

- Avoid **backtracking traps** by **limiting `.*` usage**:

  ``` python
  # Bad (greedy match)
  re.search(r"<.*>", "<div>content</div>")  # Matches "<div>content</div>"

  # Good (lazy match)
  re.search(r"<.*?>", "<div>content</div>")  # Matches "<div>"
  ```

------------------------------------------------------------------------

## **Conclusion**

🚀 **Regex is powerful for text search, validation, and extraction.** ✔ Learn the basic **symbols** (`.`, `*`, `?`, `{}`)\
✔ Use **groups & lookaheads** for flexible patterns\
✔ Apply regex for **emails, passwords, phone numbers, logs**\
✔ Optimize with **compiled regex** and **lazy matches**

------------------------------------------------------------------------

Back to top
