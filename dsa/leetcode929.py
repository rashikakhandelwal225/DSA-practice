def numUniqueEmails(emails):
    list1 = []
    for email in emails:
        head , sep, tail = email.partition("@")
        # print(head)
        # print(tail)

        head = head.replace(".","")
        # print(head)
        head = head.split("+", 1)   #1 here means 1st occurrence of + and return the splitted chars in the array form
        substring = head[0]
        email = substring + "@" + tail
        list1.append(email)
    return len(set(list1))

emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(numUniqueEmails(emails))
emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
print(numUniqueEmails(emails))