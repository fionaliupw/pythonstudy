#_*_coding:utf-8*_
#Author:Fiona

import re

#主函数
def main():

    expression = input('请输入需要计算的表达式:')
    exp = ''.join(expression.split())

    while True:
        if '(' in exp:
            re_exp = re.search(r'\(([^()]+)\)', exp)
            if re_exp is not None:
                re_exp = re_exp.groups()[0]
                re_exp = func_count(re_exp)
                exp = re.sub(r'\(([^()]+)\)', str(re_exp), exp, 1)
        else:
            re_exp = func_count(exp)
            print(re_exp)
            break
#加减法计算函数
def add_mini_func(exp):
    if '--' in exp:
        exp = exp.replace('--', '+')

    re_exp = re.findall(r'-?\d+\.?\d*', exp)
    ls = []
    for i in re_exp:
        ls.append(float(i))
    rest = sum(ls)
    return rest

#除法计算函数
def div_func(exp):
    re_exp = re.search(r'\d+\.?\d*(\/-?\d+\.?\d*)+', exp)
    if re_exp is not None:
        re_exp = re_exp.group()
        re_exp = re.findall(r'-?\d+\.?\d*', re_exp)
        ls =[]
        for i in re_exp:
            ls.append(float(i))
        rest = ls[0]
        for i1 in range(1,len(ls)):
            rest = rest / ls[i1]
        exp = re.sub(r'\d+\.?\d*(\/-?\d+\.?\d*)+', str(rest), exp, 1)
        return exp
#乘法计算函数
def mul_func(exp):
    re_exp = re.search(r'\d+\.?\d*(\*-?\d+\.?\d*)+', exp)
    if re_exp is not None:
        re_exp = re_exp.group()
        rest = 1
        re_exp = re.findall(r'-?\d+\.?\d*', re_exp)
        ls =[]
        for item in re_exp:
            ls.append(float(item))
        for i1 in range(len(ls)):
            rest = rest * ls[i1]
        exp = re.sub(r'\d+\.?\d*(\*-?\d+\.?\d*)+', str(rest), exp, 1)
        return exp
#表达式综合计算函数
def func_count(exp):
    while True:
        if '*' in exp:
            re_exp = exp.split('*')
            if '/' in re_exp[0]:
                exp = div_func(exp)
            else:
                exp = mul_func(exp)
        elif '/' in exp:
            exp = div_func(exp)

        elif '+' or '-' in exp:
            exp = add_mini_func(exp)
            return exp
        else:
            return exp

#调用main()函数
main()