'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n):

    if n < 0:       # Can't eat less than 0 cookies
        return 0
    elif n == 0:    # Can't eat 0 cookies
        return 1
    else: 
        return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)




    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 26

    print('\n')
    print(
        """
              .---. .---. 
             :     : o   :    me want cookie!
         _..-:   o :     :-.._    /
     .-''  '  `---' `---' "   ``-.    
   .'   "   '  "  .    "  . '  "  `.  
  :   '.---.,,.,...,.,.,.,..---.  ' ;
  `. " `.                     .' " .'
   `.  '`.                   .' ' .'
    `.    `-._           _.-' "  .'  .----.
      `. "    '"--...--"'  . ' .'  .'  o   `.
      .'`-._'    " .     " _.-'`. :       o  :
    .'      ```--.....--'''    ' `:_ o       :
  .'    "     '         "     "   ; `.;";";";'
 ;         '       "       '     . ; .' ; ; ;
;     '         '       '   "    .'      .-'
'  "     "   '      "           "    _.-'
        """
        )
    print('---------------------')
    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
    print('---------------------')
    print('\n')
