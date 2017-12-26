#Create a BlogPost class that has
#an author_name
#a title
#a text
#a publication_date
#Create a few blog post objects:
# "Lorem Ipsum" titled by John Doe posted at "2000.05.04."
# Lorem ipsum dolor sit amet.
# "Wait but why" titled by Tim Urban posted at "2010.10.10."
# A popular long-form, stick-figure-illustrated blog about almost everything.
# "One Engineer Is Trying to Get IBM to Reckon With Trump" titled by William Turton at "2017.03.28."  # nopep8
# Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing.  # nopep8


class BlogPost():
    author_name = ""
    title = ""
    publication_date = ""
    text = ""


blogpost_first = BlogPost()
blogpost_second = BlogPost()
blogpost_third = BlogPost()

blogpost_first.author_name = "John Doe"
blogpost_first.title = "Lorem Ipsum"
blogpost_first.publication_date = "2000.05.04"
blogpost_first.text = "Lorem ipsum dolor sit amet."

blogpost_second.author_name = "Tim Urban"
blogpost_second.title = "Wait, but why?"
blogpost_second.publication_date = "2010.10.10"
blogpost_second.text = "A popular long-form, stick-figure-illustrated blog about almost everything."  # nopep8

blogpost_third.author_name = "William Turton"
blogpost_third.title = "One Engineer Is Trying to Get IBM to Reckon With Trump"
blogpost_third.publication_date = "2017.03.28"
blogpost_third.text = "Daniel Hanley, a cybersecurity engineer at IBM, doesn’t want to be the center of attention. When I asked to take his picture outside one of IBM’s New York City offices, he told me that he wasn’t really into the whole organizer profile thing."  # nopep8
