# jQuery Web Development Project

## Learning Objectives

Explaining the following concepts without relying on external resources:

### General
- Understand the ease of front-end programming with jQuery.
- Select HTML elements in JavaScript.
- Select HTML elements using jQuery.
- Differentiate between ID, class, and tag name selectors.
- Modify HTML element styles.
- Retrieve and update HTML element content.
- Manipulate the Document Object Model (DOM).
- Make a GET request with jQuery Ajax.
- Make a POST request with jQuery Ajax.
- Listen/bind to DOM events.
- Listen/bind to user events.

### Copyright - Plagiarism

- Develop solutions independently, meeting learning objectives.
- Prohibit publishing of project content.
- Strictly avoid any form of plagiarism.

## Requirements

### General
- Editors allowed: vi, vim, emacs.
- Interpret code on Chrome (version 57.0).
- All files end with a new line.
- Mandatory README.md file at the root of the project folder.
- Code should be semistandard compliant with the flag `--global $`: `semistandard *.js --global $`.
- Use jQuery version 3.x.
- Avoid using `var`.
- HTML should not reload for each action, including DOM manipulation, value updates, and data fetching.

## More Information

### Import jQuery
```html
<head>
    <script src="https://code.jquery.com/jquery-3.2.1.min.js"></script>
</head>
```

### Manual QA Review
Request a review from a peer before the project’s deadline. If no peers are available, request a review from a TA or staff member.

## Tasks

### Task 0: No jQuery
Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`). 
Use `document.querySelector` to select the HTML tag. Do not use the jQuery API.

```html
Repo:
GitHub repository: alx-higher_level_programming
Directory: 0x15-javascript-web_jquery
File: 0-script.js
```

### Task 1: With jQuery
Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`). 
Use the jQuery API. Do not use `document.querySelector`.

```html
Repo:
GitHub repository: alx-higher_level_programming
Directory: 0x15-javascript-web_jquery
File: 1-script.js
```


## Advanced Tasks

### Task 10: No jQuery - document loaded
Write a JavaScript script that updates the text color of the `<header>` element to red (`#FF0000`). 
Use `document.querySelector` to select the HTML tag. Do not use the jQuery API. Import the script from the `<head>` tag.

```html
Repo:
GitHub repository: alx-higher_level_programming
Directory: 0x15-javascript-web_jquery
File: 100-script.js
```

### Task 11: List, add, remove
Write a JavaScript script that adds, removes, and clears `<li>` elements from a list when the user clicks. Follow the specified requirements.

```html
Repo:
GitHub repository: alx-higher_level_programming
Directory: 0x15-javascript-web_jquery
File: 101-script.js
```

### Task 12: Say hello to everybody!
Write a JavaScript script that fetches and prints how to say “Hello” depending on the language using an API service.

```html
Repo:
GitHub repository: alx-higher_level_programming
Directory: 0x15-javascript-web_jquery
File: 102-script.js
```

### Task 13: And press ENTER
Write a JavaScript script that fetches and prints how to say “Hello” depending on the language. 
The translation must be fetched when the user clicks on `INPUT#btn_translate` or presses ENTER when the focus is on `INPUT#language_code`.

```html
Repo:
GitHub repository: alx-higher_level_programming
Directory: 0x15-javascript-web_jquery
File: 103-script.js
```
