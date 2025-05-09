# [13,-3,-25,20,-3,-16,-23,18]
# #find max subarray low
# [13,-3,-25,20]      #[-3,-16,-23,18]
#
#     find max subarray low(0,1)
#     [13,-3]         #[-25,20]
#         find max subarray los(0,0)
#         [13]  #-3
#             return 13
#         find max subarray high(1,1)
#         [-3]
#             return -3
#         find max crossing(0,1,1)
#         [13, -3]
#             return (0,1,10)
#         left sum > everything (13>-3 and 10)
#             return (0,0,13)
#     find max subarray high (2,3)
#     [-25,20]
#         find max subarray low(2,2)
#         .
#         find max crossing(2,3)
#         [-25,20]
#             return (2,3,-5)
#         find max high(3,3)
#             return(20)
#         right sum > everything (20> -25 and -5)
#             return(3,3,20)
#     find max crossing(0,2,3)
#         return (0,3,5)
#     right sum > everything (5<13<20)
#         return (3,3,20)
#
# max subarraqy of first 4 arrays is [20]

#divide
#conquer
#combine
