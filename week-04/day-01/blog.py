# Blog

# Reuse your BlogPost class
# Create a Blog class
# list of BlogPosts
# add BlogPosts to your list
# delete(int) one item at given index
# update(int, BlogPost) one item at the given index and update it with another BlogPost

from blog_post import BlogPost

class Blog:
    def __init__(self):
        self.blog = [BlogPost(), BlogPost()]

    def delete(self):
        self.blog.remove(self.blog[0])
    
    def update(self):
        self.blog.append(BlogPost())

blog_list = Blog()
blog_list.blog[1]
blog_list.delete()
blog_list.update()