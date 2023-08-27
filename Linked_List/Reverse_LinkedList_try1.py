# Given the 'head' of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

class Linked_List(object):
    def reverse_LL(self, head : list) -> list:
        return_list = []
        for i in head:
            target_index = 0 - (head.index(i) + 1)
            return_list.append(head[target_index])
        
        return return_list
    
head = [1,3,5,6,6,7]
print(Linked_List().reverse_LL(head))


