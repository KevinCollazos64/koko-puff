print('\n----------------------TRIE-------------------------\n')

# EOS = End of String

print('\n- Tree based data structure that organizes information in a hierarchy\n'
      'Trie are often used with strings; Stores words for fast look-ups\n'
      '\nTrie stores a character in each node, making it efficient for prefix matching in English\n'
      '\nTRIE PROPERTIES:\n'
      '1) Used to store/search strings in time and space efficient way\n'
      '2) Any node in trie can store non repetitive multiple characters\n'
      '3) Every node stores link of next character of the string\n'
      '4) Every node keeps track of "end of string"\n')

# Each node can have any # of children
# In each node we can store any number of characters, and these characters can have multiple links to different children
# The "." in some nodes indicates end of string (boolean value T/F)
# Tries are useful for spelling checkers, and auto-completion of strings features

print('\n----------------------TRIE CREATION-------------------------\n')
# 2 classes; Trie node, and Trie system itself
# Node class should have children, and end of string property


class TrieNode:
    def __init__(self):
        self.children = {}  # we use a dict bc we need to create a link between children
        self.endofstring = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertString(self, word):
        current = self.root  # mark root node as current node
        for i in word:  # loop through word, checking if char. exists in Trie. If exists, no insert. If DNE, insert
            ch = i  # create another variable and set it to i, to show this is char.
            node = current.children.get(ch)  # checks if char. exists in the children (dict.get)
            if node is None:  # if exists, returns a node cell where we can set curr node to new node
                node = TrieNode()  # if DNE we create new node and update children of this node to the new node
                current.children.update({ch: node})
                current = node
                current.endofstring = True
                print('Successfully Inserted!')

    def searchString(self, word):
        currentnode = self.root  # locate currentnode. When we loop any given str, first node will be root
        for i in word:  # loop through character one by one
            node = currentnode.children.get(i)  # gets node for ch., if exists, we continue. if DNE, returns False
            if node is None:
                return False  # If this is satisfied, means node DNE in our Trie
            currentnode = node  # Otherwise we set currentnode to this node which will be the next node
        if currentnode.endofstring is True:
            return True
        else:
            return False

    def deleteString(self, word, index):  # index of character in the word
        ch = word[index]  # find our first character: character will be the word using index
        currentnode = self.root.children.get(ch)  # find currentnode (based on ch)
        canThisNodebeDeleted = False  # lets us know if we can safely delete

        # Case 1:
        if len(currentnode.children) > 1:  # If this cond satisfied, means we can't delete (children >1) so we continue
            Trie.deleteString(currentnode, word, index+1)  # to the next node recursively (index +1)
            return False  # we ret false b/c we assign return that comes from this method to "canthisbedeleted"
        # Case 2:
        if index == len(word) - 1:  # If this cond satisfied, means that we are at the last node. In last node we can't
            if len(currentnode.children) >= 1:  # delete b/c this string is prefix of another string.
                currentnode.endofstring = False  # so we just set EOS to false
                return False  # ret false b/c we are not deleting
            else:  # If no other node depends on ch. we just delete that ch. node
                self.root.children.pop(ch)
                return True  # if not prefix for some other word, since this is last ch., we should return True
                # to indicate we can delete
        # Case 3:
        if currentnode.endofstring == True:  # If EOS = true, can't delete, so we go to next node
            Trie.deleteString(currentnode, word, index+1)
            return False
        # Case 4:
        canThisNodebeDeleted = Trie.deleteString(currentnode, word, index+1)
        if canThisNodebeDeleted is True:
            self.root.children.pop(ch)
            return True
        else:
            return False



newTrie = Trie()


print('\n----------------------TRIE STRING INSERTION-------------------------\n')
# 4 cases:

# 1) Trie is blank (we just create node, and assign characters to this node)

# 2) New string's prefix is common to another string's prefix (we insert the remaining char. after last common trie)

# 3) New string's prefix is already present in a complete string (insert new char. at the node where we denoted EOS)

# 4) String to be inserted is already presented in Trie (don't insert anything new, just check if all elements present)

newTrie.insertString('Hello')

print('\n----------------------TRIE STRING SEARCH-------------------------\n')
# 3 cases:

# 1) String DNE (compare first ch. w/ rootnode (ex: search BCD in API. ... B != A which means str DNE in Trie) ret False

# 2) String DE (compare first ch. w/ rootnode (ex: search API in API... ch. match, but in Trie also need node for EOS)
# if node for EOS present, return True

# 3) String is a prefix of another string, but does not exist in Trie (for ex, "A" and "P" can exist as separate element
# in Trie but "AP" does not exist as a str (lacks node that denotes it is EOS)

print(newTrie.searchString('Hello'))

print('\n----------------------TRIE STRING DELETION-------------------------\n')
# Deletion of any str in Trie starts from leaf, then goes up to root
# 3 cases:

# 1) Some other prefix is same as the one we want to delete (API, APPLE)
# - check if str exists in Trie. Then start from last node and go up 1 by 1, checking if there is node that depends on
# another node. If not, we delete and continue up the Tre repeating the same steps

# 2) Str is prefix of another string (API, APIS)
# - Update EOS to False, so Trie doesn't recognize this str as a complete str
# Ex) Start at (A), then (P), (I), then (S.) ... Just delete (.) so its no longer a complete str in the Trie
# (.) denotes that its parent node is the last character

# 3) Other string is prefix of the string (APIS, AP)
# - Start from leaf. Delete (.) so no other str will be impacted. Now no EOS for APIS. Continue to next node (S)
# - Can delete (S) b/c other nodes are not impacted
# - Next is (I.) We know that when we show EOS, we just create empty node. So (I.) -> (.)

# 4) No node depends on the string (K, APIS)
# - Check if any node depends on it. Go to child node and check. No link from (K) to another node. Next node shows (.)
# - We can delete (.), then remove (K) from (AK) -> (A)


