__author__ = 'Claudia'
import sys
import os

gui_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Gui'))
packages_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Packages'))
redist_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Redist'))
plugins_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Plugins'))
fuzzy_dir = os.path.join(redist_dir, 'fuzzy')

sys.path.append(gui_dir)
sys.path.append(packages_dir)
sys.path.append(redist_dir)
sys.path.append(plugins_dir)
sys.path.append(fuzzy_dir)

from Redist.pyfuzzy.System import System
from Redist.pyfuzzy.InputVariable import InputVariable
from Redist.pyfuzzy.OutputVariable import OutputVariable
from Redist.pyfuzzy.Rule import Rule
from Redist.pyfuzzy.Adjective import Adjective
from Redist.pyfuzzy.set.Polygon import Polygon
from Redist.pyfuzzy.operator.Compound import Compound
from Redist.pyfuzzy.operator.Input import Input
from Redist.pyfuzzy.fuzzify.Plain import Plain
from Redist.pyfuzzy.defuzzify.COG import COG
import Redist.pyfuzzy.norm as norm

fuzzy_System = System(description ='LifeSystem')

input_love = InputVariable(fuzzify=Plain(),description='age',min= 0.,max = 14.)
input_love.adjectives['lots']= Adjective(Polygon([(0.,0.),(0.,1.),(2.,1.),(6.,0.)]))
input_love.adjectives['few'] = Adjective(Polygon([(0.,0.),(0.,1.),(2.,1.),(6.,0.)]))

input_health = InputVariable(fuzzify=Plain(),description='weight',min= 0.,max = 8.)
input_health.adjectives['healthy']= Adjective(Polygon([(0.,0),(0.,1.),(2.,1.),(4.,0.)]))
input_health.adjectives['sick'] = Adjective(Polygon([(0.,0),(0.,1.),(2.,1.),(4.,0.)]))

input_money = InputVariable(fuzzify=Plain(),description='weight',min= 0.,max = 8.)
input_money.adjectives['lots']= Adjective(Polygon([(0.,0),(0.,1.),(2.,1.),(4.,0.)]))
input_money.adjectives['medium'] = Adjective(Polygon([(0.,0),(0.,1.),(2.,1.),(4.,0.)]))
input_money.adjectives['few'] = Adjective(Polygon([(0.,0),(0.,1.),(2.,1.),(4.,0.)]))

fuzzy_System.variables['Love']=input_love
fuzzy_System.variables['Health'] = input_health
fuzzy_System.variables['Money'] = input_money

INF = norm.AlgebraicProduct.AlgebraicProduct()
ACC = norm.AlgebraicSum.AlgebraicSum()
COM = norm.AlgebraicSum.AlgebraicSum()
CER = norm.AlgebraicProduct.AlgebraicProduct()
COG = COG(INF=INF,ACC=ACC,failsafe = 4.)

output_happiness = OutputVariable(defuzzify=COG,description = 'Happiness',min = 1.,max=10.)
output_happiness.adjectives['sad'] = happiness_sad=Adjective(Polygon([(-1.,0),(0.,1.),(1.,1.),(3.,0.)]))
output_happiness.adjectives['normal'] =happiness_normal= Adjective(Polygon([(-1.,0),(0.,1.),(1.,1.),(3.,0.)]))
output_happiness.adjectives['happy'] =happiness_happy =Adjective(Polygon([(5.,0.),(7.,1.),(10.,1.),(11.,0)]))
output_happiness.adjectives['very_happy'] =happiness_very_happy =Adjective(Polygon([(5.,0.),(7.,1.),(10.,1.),(11.,0)]))

output_love_to_send = OutputVariable(defuzzify=COG,description = 'LoveToSend',min = 1.,max=10.)
output_love_to_send.adjectives['lots'] = love_to_send_lots =Adjective(Polygon([(-1.,0),(0.,1.),(1.,1.),(3.,0.)]))
output_love_to_send.adjectives['medium'] = love_to_send_medium= Adjective(Polygon([(-1.,0),(0.,1.),(1.,1.),(3.,0.)]))
output_love_to_send.adjectives['few'] = love_to_send_few =Adjective(Polygon([(5.,0.),(7.,1.),(10.,1.),(11.,0)]))

fuzzy_System.variables['LoveToSend'] = output_love_to_send
fuzzy_System.variables['HappinessAmount'] = output_happiness



fuzzy_System.rules['happiness1'] =\
Rule(adjective=happiness_sad,operator=Compound(norm.FuzzyOr()
    ,Compound(norm.FuzzyOr()
        ,Input(fuzzy_System.variables['Love'].adjectives['few'])
        ,Input(fuzzy_System.variables['Health'].adjectives['sick']))
    ,Input(fuzzy_System.variables['Money'].adjectives['few'])),CER = CER)

fuzzy_System.rules['happiness2'] =\
Rule(adjective=happiness_very_happy,operator=Compound(norm.FuzzyAnd()
    ,Compound(norm.FuzzyAnd()
        ,Input(fuzzy_System.variables['Love'].adjectives['lots'])
        ,Input(fuzzy_System.variables['Health'].adjectives['healthy']))
    ,Input(fuzzy_System.variables['Money'].adjectives['lots'])),CER = CER)

fuzzy_System.rules['happiness3'] =\
Rule(adjective=happiness_normal,operator=Compound(norm.FuzzyOr()
    ,Compound(norm.FuzzyOr()
        ,Input(fuzzy_System.variables['Love'].adjectives['lots'])
        ,Input(fuzzy_System.variables['Health'].adjectives['healthy']))
    ,Input(fuzzy_System.variables['Money'].adjectives['lots'])),CER = CER)

fuzzy_System.rules['happiness4'] =\
Rule(adjective=happiness_happy,operator=Compound(norm.FuzzyAnd()
    ,Input(fuzzy_System.variables['Love'].adjectives['lots'])
    ,Input(fuzzy_System.variables['Health'].adjectives['healthy'])),CER = CER)

fuzzy_System.rules['happiness5'] =\
Rule(adjective=happiness_happy,operator=Compound(norm.FuzzyAnd()
    ,Input(fuzzy_System.variables['Money'].adjectives['lots'])
    ,Input(fuzzy_System.variables['Health'].adjectives['healthy'])),CER = CER)

fuzzy_System.rules['happiness6'] =\
Rule(adjective=happiness_happy,operator=Compound(norm.FuzzyAnd()
    ,Input(fuzzy_System.variables['Love'].adjectives['lots'])
    ,Input(fuzzy_System.variables['Money'].adjectives['lots'])),CER = CER)


fuzzy_System.rules['love_to_send1'] =\
Rule(adjective=love_to_send_lots,operator=Compound(norm.FuzzyAnd()
    ,Input(fuzzy_System.variables['Love'].adjectives['lots'])
    ,Input(fuzzy_System.variables['Money'].adjectives['lots'])),CER = CER)

fuzzy_System.rules['love_to_send2'] =\
Rule(adjective=love_to_send_lots,operator=Compound(norm.FuzzyAnd()
    ,Input(fuzzy_System.variables['Love'].adjectives['lots'])
    ,Input(fuzzy_System.variables['Health'].adjectives['healthy'])),CER = CER)

fuzzy_System.rules['love_to_send3'] =\
Rule(adjective=love_to_send_lots,operator=Compound(norm.FuzzyAnd()
    ,Compound(norm.FuzzyAnd()
        ,Input(fuzzy_System.variables['Love'].adjectives['lots'])
        ,Input(fuzzy_System.variables['Health'].adjectives['healthy']))
    ,Input(fuzzy_System.variables['Money'].adjectives['lots'])),CER = CER)

fuzzy_System.rules['love_to_send4'] =\
Rule(adjective=love_to_send_medium,operator=Compound(norm.FuzzyAnd()
    ,Input(fuzzy_System.variables['Love'].adjectives['few'])
    ,Input(fuzzy_System.variables['Health'].adjectives['healthy'])),CER = CER)

fuzzy_System.rules['love_to_send5'] =\
Rule(adjective=love_to_send_medium,operator=Compound(norm.FuzzyAnd()
    ,Input(fuzzy_System.variables['Love'].adjectives['few'])
    ,Input(fuzzy_System.variables['Money'].adjectives['lots'])),CER = CER)

fuzzy_System.rules['love_to_send6'] =\
Rule(adjective=love_to_send_medium,operator=Compound(norm.FuzzyAnd()
    ,Input(fuzzy_System.variables['Love'].adjectives['few'])
    ,Input(fuzzy_System.variables['Money'].adjectives['medium'])),CER = CER)

fuzzy_System.rules['love_to_send7'] =\
Rule(adjective=love_to_send_few,operator=Compound(norm.FuzzyAnd()
    ,Input(fuzzy_System.variables['Love'].adjectives['few'])
    ,Input(fuzzy_System.variables['Money'].adjectives['few'])),CER = CER)

fuzzy_System.rules['love_to_send8'] =\
Rule(adjective=love_to_send_few,operator=Compound(norm.FuzzyAnd()
    ,Input(fuzzy_System.variables['Love'].adjectives['few'])
    ,Input(fuzzy_System.variables['Health'].adjectives['sick'])),CER = CER)




#fuzzy_System.rules['r2'] = Rule(adjective=lots,operator=Compound(Min(),Input(fuzzy_System.variables['age_var'].adjectives['middle']),Input(fuzzy_System.variables['weight_var'].adjectives['low'])),CER = CER)
#fuzzy_System.rules['r3'] = Rule(adjective=medium,operator=Input(fuzzy_System.variables['age_var'].adjectives['middle']),CER = CER)
#fuzzy_System.rules['r4'] = Rule(adjective= medium,operator=Compound(Min(),Input(fuzzy_System.variables['age_var'].adjectives['big']),Input(fuzzy_System.variables['weight_var'].adjectives['low'])),CER=CER)
#fuzzy_System.rules['r5'] = Rule(adjective = few, operator =Input(fuzzy_System.variables['age_var'].adjectives['big']),CER =CER)

#fuzzy_System.rules['r1'] = Rule(adjective=lots,operator=Input(fuzzy_System.variables['age_var'].adjectives['little']),CER = CER)
#fuzzy_System.rules['r2'] = Rule(adjective=lots,operator=Compound(Min(),Input(fuzzy_System.variables['age_var'].adjectives['middle']),Input(fuzzy_System.variables['weight_var'].adjectives['low'])),CER = CER)
#fuzzy_System.rules['r3'] = Rule(adjective=medium,operator=Compound(Min(),Input(fuzzy_System.variables['age_var'].adjectives['middle']),Input(fuzzy_System.variables['weight_var'].adjectives['average'])),CER = CER)
#fuzzy_System.rules['r4'] = Rule(adjective= medium,operator=Compound(Min(),Input(fuzzy_System.variables['age_var'].adjectives['big']),Input(fuzzy_System.variables['weight_var'].adjectives['low'])),CER=CER)
#fuzzy_System.rules['r5'] = Rule(adjective = few, operator =Compound(Max(),Compound(Min(),Input(fuzzy_System.variables['age_var'].adjectives['big']),Input(fuzzy_System.variables['weight_var'].adjectives['average'])),Input(fuzzy_System.variables['weight_var'].adjectives['high'])),CER =CER)

#output={'milk_amount':3}
#fuzzy_System.calculate({'age_var':9,'weight_var':None},output)
#print(output['milk_amount'])