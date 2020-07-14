from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        
    def tearDown(self):
        self.browser.quit()
        
    def test_can_view_blog_posts_and_make_comments(self):
        #Bob has heard about a new blogging website. He goes to check out its homepage
        self.browser.get('http://localhost:8000')

        #He notices the page title and header mention blogs.
        self.assertIn('blog', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Blog', header_text)
       
        
        #He is able to see the list of blog posts.
        post = self.browser.find_element_by_css_selector('div.post')
        self.assertEqual(post.get_attribute('title'),'')
        
        #Bob tries to comment on a post, via the post_detail view.
        self.fail('Finish the test.')

if __name__ == '__main__':
    unittest.main(warnings='ignore')


#He is invited to sign in to the website.

#He is invited to create a new blog post.

#Bob wants to edit an existing blog post. He does this by clicking on the post in question and then clicking the edit tool.

#Bob edits the blog post accordingly, when he is done, he clicks "submit".

#He will now see the updated blog post.

#Bob wonders whether the changes he has made will be saved. He then sees that each blog post is entered as a form and stored on the model database.

#Bob wants to delete a blog post. He does this by viewing the blog post in more detail and clicking on the remove icon.

#Bob is redirected to the list of blog posts and sees that the blog is no longer present.

#Bob wishes to leave a comment on one of the blog posts. He does this by viewing the blog post in more detail, then scrolling to the bottom and clicking add new comment. He then approves his comment and sees it added to the blog post.

#Bob wishes to see what he can do as a un-authorised user so he logs out

#Bob wishes to approve any not yet approved comments. He visits every post and approves any comment that needs to be.

#Bob also views the drafted blog posts that are yet to be published by clicking on the drafts icon.

