# for j in range(1,6,1):
#     for i in range(1,6,1):
#         print(i,end=" ")
#     print()    
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
#---------------------------------------------------------------
# for j in range(1,6,1):
#     for i in range(1,6,1):
#         if(j==1):
#             print("*", end=" ")
#         else:
#             print(i, end=" ")    
#     print()       
# * * * * * 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# 1 2 3 4 5 
# ----------------------------------------------------------------
# for j in range(1,6,1):
#     for i in range(1,6,1):
#         if(j==1 or j==3 or j==5):
#             print("*", end=" ")
#         else:
#             print(i, end=" ")    
#     print()   
# * * * * * 
# 1 2 3 4 5 
# * * * * * 
# 1 2 3 4 5 
# * * * * *       
#--------------------------------------------------------------------

# for j in range(1,6,1):
#     for i in range(1,6,1):
#         if(j==1 or j==3 or j==5):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")    
#     print()   
# * * * * * 
          
# * * * * * 
          
# * * * * * 
#-----------------------------------------------------------------------

# for j in range(1,6,1):
#     for i in range(1,6,1):
#         if(i==1 or i==3 or i==5):
#             print("*", end=" ")
#         else:
#             print("", end=" ")    
#     print()   

# *  *  * 
# *  *  * 
# *  *  * 
# *  *  * 
# *  *  * 

#-----------------------------------------------------------------------

# for j in range(1,6,1):
#     for i in range(1,6,1):
#         if(i==1 or i==3 or i==5):
#             print("+", end=" ")
#         else:
#             print(i, end=" ")    
#     print()   

# + 2 + 4 + 
# + 2 + 4 + 
# + 2 + 4 + 
# + 2 + 4 + 
# + 2 + 4 + 
#-------------------------------------------------------------

# for j in range(1,8,1):
#     for i in range(1,8,1):
#         if(i==1 or j==1 or i==7 or j==7):
#             print("+", end=" ")
#         else:
#             print(" ", end=" ")    
#     print()   

# + + + + + + + 
# +           + 
# +           + 
# +           + 
# +           + 
# +           + 
# + + + + + + + 
#----------------------------------------------------------------------

# for j in range(1,8,1):
#     for i in range(1,8,1):
#         if(i==1 or i==4 or i==7 or j==1 or j==4 or j==7):
#             print("+", end=" ")
#         else:
#             print(" ", end=" ")    
#     print()   

# + + + + + + + 
# +     +     + 
# +     +     + 
# + + + + + + + 
# +     +     + 
# +     +     + 
# + + + + + + + 

#------------------------------------------------------------------------

# for j in range(1,8,1):
#     for i in range(1,8,1):
#         if(i==4 or j==1):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")    
#     print()   

#  * * * * * * * 
#       *       
#       *       
#       *       
#       *       
#       *       
#       *       

#----------------------------------------------------------------------------------

# for j in range(1,8,1):
#     for i in range(1,8,1):
#         if(i==4 or j==1 and i<=4 ):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")    
#     print()   

# * * * *       
#       *       
#       *       
#       *       
#       *       
#       *       
#       *       
#------------------------------------------------------------------------------

# for j in range(1,8,1):
#     for i in range(1,8,1):
#         if(i==4 or j==1 and i<=4 or j==7):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")    
#     print()   

# * * * *       
#       *       
#       *       
#       *       
#       *       
#       *       
# * * * * * * * 

#-----------------------------------------------------------------------------

# for j in range(1,8,1):
#     for i in range(1,8,1):
#         if(i==4 or j==1 and i<=4 or j==7 and i>=4 or j==4 or i==1 and j>=4 or i==7 and j<=4):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")    
#     print()   

# * * * *     * 
#       *     * 
#       *     * 
# * * * * * * * 
# *     *       
# *     *       
# *     * * * * 

#--------------------------------------------------------------------------
# for j in range(1,8,1):
#     for i in range(1,8,1):
#         if(i==j):
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")    
#     print()   

# *             
#   *           
#     *         
#       *       
#         *     
#           *   
#             * 
#--------------------------------------------------------------------------
# for j in range(1,8,1):
#     for i in range(1,8,1):
#         if(i==j or j+i==8 ):
#             print("*", end=" ")
#         else:
#             print("", end=" ")    
#     print() 

# *      * 
#  *    *  
#   *  *   
#    *    
#   *  *   
#  *    *  
# *      * 

# for j in range(1,6,1):
#     for i in range(1,6,1):
#         if(i==1 or i==3 or i==5) or (j==1 or j==3 or j==5 ) or (i==j or i+j==6):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")    
#     print()       

#---------------------------------------------------------------------------
# for j in range(1,10,1):
#     for i in range(1,10,1):
#         if(i==5 and j>=5 or i==j and j<=5 or i+j==10 and i>=5):
#             print("*", end=" ")
#         else:
#             print("", end=" ")    
#     print()   

# *        * 
#  *      *  
#   *    *   
#    *  *    
#     *     
#     *     
#     *     
#     *     
#     *     
#------------------------------------------------------------------

# for j in range(1,8,1):
#     for i in range(1,8,1):
#         if j==1 or i==1 or j==7 or i==7 or j==4 or i==4 or j==i or i==7 or j+i==8:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()   

# * * * * * * * 
# * *   *   * * 
# *   * * *   * 
# * * * * * * * 
# *   * * *   * 
# * *   *   * * 
# * * * * * * *      
# -------------------------------------------------------------------      

# for j in range(1,8,1):
#     for i in range(1,8,1):
#         if i==4 and j>=4 or i==j and j<=4 or j+i==8 and j<=4:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()   

#  *           * 
#   *       *   
#     *   *     
#       *       
#       *       
#       *       
#       *       

#-----------------------------------------------------------------
# for j in range(1,6,1):
#     for i in range(1,6,1):
#         if (i==1 and j<=3) or (j==3 or i==5 and j>=3) or (i==3 or j==5 and i<=3) or (j==1 and i>=3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")   
#     print()     

# *   * * * 
# *   *     
# * * * * * 
#     *   * 
# * * *   *     
#-----------------------------------------------------------------

# for j in range(1,8,1):
#     for i in range(1,8,1):
#         if i+j==5 or j==4 or i-j==3 or j==2 or j==5 and i==4:  
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")   
#     print()     

#       *       
# * * * * * * * 
#   *       *   
# * * * * * * * 
#       *       
#------------------------------------------------------------------

# for j in range(1,10,1):
#     for i in range(1,10,1):
#         if i+j==6 or j==3 or j==5 or i-j==4 or j==6 and i==4 or j==7 and i==5:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()            

# for j in range(1,8,1):
#     for i in range(1,10,1):
#         if i+j==6 or j==3 or j==5 or i-j==4 :
#             print("*",)

# for j in range(1,6,1):
#     for i in range(1,8,1):
#         if  j==1 or i==1 and j<=4 or j==5 or i==7 or j==3 :
#             print("*",end="")
#         else:
#             print("",end=" ")    
#     print()  
          
# *******
# *     *
# *******
# *     *
# *******

# # square problem
# n = 5
# for i in range(n):
#     for j in range(n):
#         print("* ", end=" ")
#     print()
# # *  *  *  *  *  
# # *  *  *  *  *  
# # *  *  *  *  *  
# # *  *  *  *  *  
# # *  *  *  *  *     

# # Right Angle triangle problem
# n = 5
# for i in range(1, n+1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# # * 
# # * * 
# # * * * 
# # * * * * 
# # * * * * * 

# # Inverted right angle triangle problem
# n = 5
# for i in range(n, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# # * * * * * 
# # * * * * 
# # * * * 
# # * * 
# # * 

# # Pyramid problem
# n = 5
# for i in range(1, n+1):
#     print(" " * (n-i), end="")
#     print("* " * i)

# #     * 
# #    * * 
# #   * * * 
# #  * * * * 
# # * * * * * 

# # Number pyramid problem
# n = 5
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(j, end=" ")
#     print()

# # 1 
# # 1 2 
# # 1 2 3 
# # 1 2 3 4 
# # 1 2 3 4 5 

# # Diamond Pattern problem
# n = 5
# for i in range(1, n+1):
#     print(" "*(n-i) + "*"*(2*i-1))
# for i in range(n-1, 0, -1):
#     print(" "*(n-i) + "*"*(2*i-1))
# #     *
# #    ***
# #   *****
# #  *******
# # *********
# #  *******
# #   *****
# #    ***
# #     *

# # Floyd's Triangle problem
# n = 5
# num = 1
# for i in range(1, n+1):
#     for j in range(i):
#         print(num, end=" ")
#         num += 1
#     print()

# # 1 
# # 2 3 
# # 4 5 6 
# # 7 8 9 10 
# # 11 12 13 14 15

# # Pascal's Triangle problem
# n = 5
# for i in range(n):
#     val = 1
#     print(" "*(n-i), end="")
#     for j in range(i+1):
#         print(val, end=" ")
#         val = val * (i-j) // (j+1)
#     print()

# #      1 
# #     1 1 
# #    1 2 1 
# #   1 3 3 1 
# #  1 4 6 4 1 