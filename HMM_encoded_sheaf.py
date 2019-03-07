"""Metin Toksoz-Exley- Research Sheaf Construction - October 2018"""
import math 
import numpy as np 
import pysheaf as ps 
 
# Metrics and spherical geometry
# Cell: name = stalk (variables)
#X=WxPxF 
#U1=F we never actually use this index because diagram commutes 
#U2=PxF
#U3=WxF
#U4=WxP
#V1=P
#V2=F
#V3=W
#difference between LINEAR morphism and SET morphism 
s1=ps.Sheaf([ps.SheafCell(dimension=0,
                          compactClosure=True,
                          stalkDim=2, #THIS IS THE NUMBER OF COLUMNS ?!?!
                          cofaces=[ps.SheafCoface(index=4,
                                                  orientation=1,
                                                  restriction=ps.LinearMorphism(np.array([[1.0, 0],
                                                                                          [0, 1.0]]))), #X>U3 ?!?!?!
                                   ps.SheafCoface(index=5,
                                                  orientation=-1,
                                                  restriction=ps.LinearMorphism(np.array([[0, 0],
                                                                                          [1.0, 0],
                                                                                          [0, 1.0],
                                                                                          [0, 0]])))]), #X>U4
            ps.SheafCell(dimension=0,
                          compactClosure=True,
                          stalkDim=4, #WHICH INDEX OF COLUMNS IS THIS REFERRING TO, THE SEED OR THE FINALS
                          cofaces=[ps.SheafCoface(index=4,
                                                  orientation=1,
                                                  restriction=ps.LinearMorphism(np.array([[1.0, 1.0, 0, 0],
                                                                                          [0, 0, 1.0, 1.0]]))), #X>U3 ?!?!?
                                    ps.SheafCoface(index=5,
                                                  orientation=-1,
                                                  restriction=ps.LinearMorphism(np.array([[1.0, 0, 0, 0],
                                                                                          [0, 1.0, 0, 0],
                                                                                          [0, 0, 1.0, 0],
                                                                                          [0, 0, 0, 1.0]
                                                                                          ])))]), #X>U4
            ps.SheafCell(dimension=0,
                          compactClosure=True,
                          stalkDim=4, #THIS IS THE NUMBER OF COLUMNS 
                          cofaces=[ps.SheafCoface(index=5,
                                                  orientation=1,
                                                  restriction=ps.LinearMorphism(np.array([[1.0, 0, 0, 0],
                                                                                          [0, 1.0, 0, 0],
                                                                                          [0, 0, 1.0, 0],
                                                                                          [0, 0, 0, 1.0]]))),
                                   ps.SheafCoface(index=6,
                                                  orientation=-1,
                                                  restriction=ps.LinearMorphism(np.array([[1.0, 0, 1.0, 0],
                                                                                          [0, 1.0, 0, 1.0]])))]), #V3>V3
            ps.SheafCell(dimension=0,
                          compactClosure=True,
                          stalkDim=2, #THIS IS THE NUMBER OF COLUMNS 
                          cofaces=[ps.SheafCoface(index=5,
                                                  orientation=1,
                                                  restriction=ps.LinearMorphism(np.array([[1.0, 0],
                                                                                          [0, 0],
                                                                                          [0, 0],
                                                                                          [0, 1.0]]))), #X>U4
                                   ps.SheafCoface(index=6,
                                                  orientation=-1,
                                                  restriction=ps.LinearMorphism(np.array([[1.0, 0],
                                                                                          [0, 1.0]])))]), #V3>V3
            ps.SheafCell(dimension=1,
                          compactClosure=True,
                          stalkDim=2, #THIS IS THE NUMBER OF rows 
                          cofaces=[]),
            ps.SheafCell(dimension=1,
                          compactClosure=True,
                          stalkDim=4, #THIS IS THE NUMBER OF rows 
                          cofaces=[]),
            ps.SheafCell(dimension=1,
                          compactClosure=True,
                          stalkDim=2, #THIS IS THE NUMBER OF rows 
                          cofaces=[])
])
#SUPPORT NEEDS TO MATCH INDEX OF THAT ARRAY
            
input_data=[ps.Section([ps.SectionCell(support=0,value=np.array([0.5, 0.5])), # X
                        #ps.SectionCell(support=1,value=np.array([]),  U1 WE DON'T ACTUALLY REFERENCE U1 SINCE NOT IN DIAGRAM
                        ps.SectionCell(support=1,value=np.array([0.5, 0.5, 0.5, 0.5])), # U2
                        ps.SectionCell(support=2,value=np.array([0.5, 0.5, 0.5, 0.5])), # U3
                        ps.SectionCell(support=3,value=np.array([0.5, 0.5])), # U4
                        ps.SectionCell(support=4,value=np.array([0, 0])), # V1
                        ps.SectionCell(support=5,value=np.array([0, 0, 0, 0])), # V2
                        ps.SectionCell(support=6,value=np.array([0, 0]))])] # V3
                        
""" THIS IS ALL BOTTOM CELLS HAVE 1/2 
input_data=[ps.Section([ps.SectionCell(support=0,value=np.array([0.5, 0.5])), # X
                        #ps.SectionCell(support=1,value=np.array([]),  U1 WE DON'T ACTUALLY REFERENCE U1 SINCE NOT IN DIAGRAM
                        ps.SectionCell(support=1,value=np.array([0.5, 0.5, 0.5, 0.5])), # U2
                        ps.SectionCell(support=2,value=np.array([0.5, 0.5, 0.5, 0.5])), # U3
                        ps.SectionCell(support=3,value=np.array([0.5, 0.5])), # U4
                        ps.SectionCell(support=4,value=np.array([0, 0])), # V1
                        ps.SectionCell(support=5,value=np.array([0, 0, 0, 0])), # V2
                        ps.SectionCell(support=6,value=np.array([0, 0]))])] # V3
                        """
            #only one section, 
# Exhibit the consistency radius of the partially-filled Section with the input data
consistency_radii=[s1.consistencyRadius(case, ord=2) for case in input_data] #should be small 
print 'Raw consistency radii for each test case: ' + str(consistency_radii)
# Perform data fusion
fused_data=[s1.fuseAssignment(case, method='KernelProj', ord=2) for case in input_data] #find nearest global sections ou=list of new sections [one] 
#print fused_data   COULD USE 'KernelProj' - , method='KernelProj' delete if want to use orig. 
# Exhibit the consistency radius of the fused data and output the final fused values.  These should be global sections, so very close to zero
fused_consistency_radii=[s1.consistencyRadius(case, ord=2) for case in fused_data] #crosscheck should be zero b/z closest 
print 'Post-fusion consistency radii for each test case (should ideally be zero!): ' + str(fused_consistency_radii)
#
## Demonstrate the consistency radius improves when faulty sensor (U5) is removed
#print 'Case 2 consistency radius after removing faulty sensor ' + str(s1.consistencyRadius(input_data[1],testSupport=[0,1,2,3,4,6,7,8]))
#print 'Case 3 consistency radius after removing faulty sensor ' + str(s1.consistencyRadius(input_data[2],testSupport=[0,1,2,3,4,6,7,8]))
#
## Perform limited data fusion in which we modify only the faulty sensor (U5)
#fused_data_U5=[s1.fuseAssignment(case,activeCells=[5]) for case in input_data]
##print fused_data
## Exhibit the consistency radius of the fused data and output the final fused values.  These may not be global sections!
#fused_consistency_radii_U5=[s1.consistencyRadius(case) for case in fused_data_U5]
#print 'Post-fusion consistency radii for each test case modifying only U5 (should be smaller than the raw case, but not zero!): ' + str(fused_consistency_radii_U5)
#print 'Change to values in stalks other than that over U5 post fusion that modifies only U5 (should be zero!): ' + str( max([np.linalg.norm(scnew.value - scold.value) for j in range(len(input_data)) for scnew in fused_data_U5[j].sectionCells for scold in input_data[j].sectionCells if scnew.support == scold.support and scold.support != 5]))


"""

compute cohomology (search in tests-sheaf tutorial page on website there's some code)
take priors (what you'rebuilding model from) and make sections out of them compute their consistency radius run bp make new section 
verify consittency radius has gone down 


would indicate bp is doing some as sheaves
consistency radius as a function of bp interations (a graph going down with each iteration) 
stabilize at zero

LOOPY WOULD CONVERGE TO NOT ZERO 
"""