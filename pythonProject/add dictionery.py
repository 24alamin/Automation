post = {
    "id":100,
    "Author":"Jolil",
    "Category":"Awesome",
    "Title":"This is awesome",
    "Conclusion":"The bottom line",
}
post["Category"] = "Genius"
post.update({"Category":"Beautiful"})
print(post)