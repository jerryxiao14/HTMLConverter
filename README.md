# HTMLConverter

This project is a simple Markdown-to-HTML converter implemented in Python. It supports headings, paragraphs, emphasis (bold/italic), ordered and unordered lists, inline code, and links.  

---

## Known Limitations

1. **Nested formatting is limited**  
   - Nested emphasis inside bold/italic may not always render correctly.  
   - Lists inside lists (nested lists) are not supported.  

2. **Underline-style headings**  
   - Only supports `===` for H1 and `---` for H2 directly below the text.  

3. **Inline edge cases**  
   - Complex combinations of inline code, links, and emphasis in the same word may not always convert perfectly.  

4. **Full Markdown support**  
   - Features like images, tables, blockquotes, and footnotes are **not implemented**.  

---

## Running Tests

1. Activate your environment:

```bash
conda activate htmlconv
```
2. Run tests with pytest:

```bash
pytest -v
```



