class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        self.reviews=list()
    
    def addReview(self,review):
        self.reviews.append(review)

    def countReviews(self):
        return len(self.reviews)
    
    def displayReviews(self):
        for review in self.reviews:
            print(review,end=" , ")
    

book1=Book("Macbeth","William Shakespear") 
book2=Book("Herry Potter","XYZ")
book1.addReview("Nice")
book1.addReview("well")
book1.addReview("Good")
print("total reviews of Book :",book1.title ," are ",book1.countReviews())
book1.displayReviews()
