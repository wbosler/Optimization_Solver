from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, LpMinimize
import streamlit as st
import pandas as pd


#Web_App headings

st.write("# Optimization Solver")
st.sidebar.header("Application Mode")
app_mode = st.sidebar.selectbox("What would you like to do?",("View the instructions and overview", "Start modelling"))


#storing variables names for optimizer as zeros or empty strings until updated

x1_obj = 0
x2_obj = 0
x3_obj = 0
x4_obj = 0
x5_obj = 0
x6_obj = 0
x7_obj = 0
x8_obj = 0
x9_obj = 0
x10_obj = 0

con1_rhs = 0
con2_rhs = 0
con3_rhs = 0
con4_rhs = 0
con5_rhs = 0
con6_rhs = 0
con7_rhs = 0
con8_rhs = 0
con9_rhs = 0
con10_rhs = 0
con11_rhs = 0
con12_rhs = 0

gl_x1_c1 = 0
gl_x2_c1 = 0
gl_x3_c1 = 0
gl_x4_c1 = 0
gl_x5_c1 = 0
gl_x6_c1 = 0
gl_x7_c1 = 0
gl_x8_c1 = 0
gl_x9_c1 = 0
gl_x10_c1 = 0

gl_x1_c2 = 0
gl_x2_c2 = 0
gl_x3_c2 = 0
gl_x4_c2 = 0
gl_x5_c2 = 0
gl_x6_c2 = 0
gl_x7_c2 = 0
gl_x8_c2 = 0
gl_x9_c2 = 0
gl_x10_c2 = 0

gl_x1_c3 = 0
gl_x2_c3 = 0
gl_x3_c3 = 0
gl_x4_c3 = 0
gl_x5_c3 = 0
gl_x6_c3 = 0
gl_x7_c3 = 0
gl_x8_c3 = 0
gl_x9_c3 = 0
gl_x10_c3 = 0

gl_x1_c4 = 0
gl_x2_c4 = 0
gl_x3_c4 = 0
gl_x4_c4 = 0
gl_x5_c4 = 0
gl_x6_c4 = 0
gl_x7_c4 = 0
gl_x8_c4 = 0
gl_x9_c4 = 0
gl_x10_c4 = 0

gl_x1_c5 = 0
gl_x2_c5 = 0
gl_x3_c5 = 0
gl_x4_c5 = 0
gl_x5_c5 = 0
gl_x6_c5 = 0
gl_x7_c5 = 0
gl_x8_c5 = 0
gl_x9_c5 = 0
gl_x10_c5 = 0

gl_x1_c6 = 0
gl_x2_c6 = 0
gl_x3_c6 = 0
gl_x4_c6 = 0
gl_x5_c6 = 0
gl_x6_c6 = 0
gl_x7_c6 = 0
gl_x8_c6 = 0
gl_x9_c6 = 0
gl_x10_c6 = 0

gl_x1_c7 = 0
gl_x2_c7 = 0
gl_x3_c7 = 0
gl_x4_c7 = 0
gl_x5_c7 = 0
gl_x6_c7 = 0
gl_x7_c7 = 0
gl_x8_c7 = 0
gl_x9_c7 = 0
gl_x10_c7 = 0

gl_x1_c8 = 0
gl_x2_c8 = 0
gl_x3_c8 = 0
gl_x4_c8 = 0
gl_x5_c8 = 0
gl_x6_c8 = 0
gl_x7_c8 = 0
gl_x8_c8 = 0
gl_x9_c8 = 0
gl_x10_c8 = 0

gl_x1_c9 = 0
gl_x2_c9 = 0
gl_x3_c9 = 0
gl_x4_c9 = 0
gl_x5_c9 = 0
gl_x6_c9 = 0
gl_x7_c9 = 0
gl_x8_c9 = 0
gl_x9_c9 = 0
gl_x10_c9 = 0

gl_x1_c10 = 0
gl_x2_c10 = 0
gl_x3_c10 = 0
gl_x4_c10 = 0
gl_x5_c10 = 0
gl_x6_c10 = 0
gl_x7_c10 = 0
gl_x8_c10 = 0
gl_x9_c10 = 0
gl_x10_c10 = 0

gl_x1_c11 = 0
gl_x2_c11 = 0
gl_x3_c11 = 0
gl_x4_c11 = 0
gl_x5_c11 = 0
gl_x6_c11 = 0
gl_x7_c11 = 0
gl_x8_c11 = 0
gl_x9_c11 = 0
gl_x10_c11 = 0

gl_x1_c12 = 0
gl_x2_c12 = 0
gl_x3_c12 = 0
gl_x4_c12 = 0
gl_x5_c12 = 0
gl_x6_c12 = 0
gl_x7_c12 = 0
gl_x8_c12 = 0
gl_x9_c12 = 0
gl_x10_c12 = 0

con1_inequality = ""
con2_inequality = ""
con3_inequality = ""
con4_inequality = ""
con5_inequality = ""
con6_inequality = ""
con7_inequality = ""
con8_inequality = ""
con9_inequality = ""
con10_inequality = ""
con11_inequality = ""
con12_inequality = ""

var_list = ['x1','x2','x3','x4','x5','x6','x7','x8','x9','x10']

#Sidebar components
def instr():
    st.write("")
    st.write("")
    overview = st.beta_expander("Overview of Application", expanded = 0 )
    with overview:
        st.write("")
        st.write("This application is intended to assist the user in designing mathematical models to solve \
        real world problems.")
        st.write("Specifically, this application will provide you with a framework to solve **Optimization Models**.\
        These models contain three primary components:")
        st.write("**1.**  An objective function")
        st.write('**2.**  A set of decision variables')
        st.write("**3.**  A set of constraints")
        st.write("")
        st.write("The goal of an optimization model is to 'optimize' (maximize/minimize) an objective function \
        by finding the best values for controllable decision variables out of all possible values that could \
        satisfy a given set of constraints.")
        st.write("Optimization models are useful in a wide range of fields from manufacturing and scheduling to \
        marketing, finance and transportation. This branch of applied mathematics can be a powerful \
        aid in increasing operational efficiency and improving outcomes by reducing reliance on adhoc methods such as \
        'guess and check' and expensive build and test phases.")
        st.write("")

    terminology = st.beta_expander("Key Terminology Explained", expanded = 0 )
    with terminology:
        st.write("")
        st.write("**Objective Function:**")
        st.write("The objective function can be viewed as a mathematical expression including your decision variables \
        that will calculate the output you want to maximize or minimize.")
        st.write("**Example:**")
        st.write("Lets assume a company sells three products and we want to maximize sales revenue. Product one sells for $2000, product two for $1000 and \
        proudct 3 sells for $5000.")
        st.write("If we define our decision variables as x1 , x2 and x3 representing the number of product 1, 2 and 3 \
        produced respectively, then our objective function is: Maximize 2000$$x_1$$ + 1000$$x_2$$ + 5000$$x_3$$")
        st.write("")
        st.write("**Decision Variables:**")
        st.write("The decision variables can be thought of as algebraic representations of things you can control \
        within the problem scope. In the earlier example our decision variables were the number of products produced.")
        st.write("")
        st.write("**Constraints:**")
        st.write("A constraint refers to a restriction on a set of decision variables that must be satisfied.\
        In the above example let's assume the company only has 100 hours of staff time available for production.\
        If product 1, 2 and 3 require 10, 5 and 13 hours of labour respectively we can reflect this using\
        the following constraint: 10$$x_1$$ + 5$$x_2$$ + 13$$x_3$$ $${\le}$$ 100")
        st.write("")



    instructions = st.beta_expander("How to Use the Application", expanded = 0 )
    with instructions:
        st.write("")
        st.write("When you are ready to begin modelling select *start modelling* from the sidebar dropdown. \
        This will activate the model interface.")
        st.write("**Suggested Work Flow**")
        st.write("**1. Input Parameters:** Begin by updating the *user input parameters* in the sidebar as to reflect the problem you wish to solve. \
        As you populate the input parameters the main window will update.")
        st.write("It is recommended that you enter all input parameters prior to editing the main window. \
        It is also recommended that you leave the *display constraints box* unchecked prior to performing the final \
        configuration review of your model however this is purely for aesthetic purposes.")
        st.write("**2. Objective Function:** Expand the *define objective function section* and enter the coefficient values. \
        Once entered the section can be minimized and your objective function viewed in the *Model \
        Configuration Summary*. If any of the numbers have been entered incorrectly simply expand the \
        objective section and re enter the correct value.")
        st.write("**3. Constraints:** Expand one of the *constraint sections* and enter the requested details. Select which \
        variables to include in the constraint from the drop down and enter the respective coefficient values. \
        Once completed minimise the constraint box and expand your next constraint if required.")
        st.write("At any time you can check your constraints have been entered correctly by selecting *display \
        constraints* in the sidebar. If a coefficient isn't entered correctly simply expand the corresponding \
        constraint and re-enter the required values.")
        st.write("**4. Configuration Summary:** Select *display constraints* in the sidebar and review both the objective \
        function and constraints in the *configuration summary*. Fix any incorrect details by repeating the \
        earlier corresponding steps and once satisfied select *confirm model and run optimisation*.")
        st.write("**5. Model Output:** In the main window an output section will populate. This will confirm \
        whether the model was successfully optimised and provide both the optimized value of the objective function \
        and your decision variables.")
        st.write("You can also view the non zero deltas to constraint bounds by selecting the checkbox \
        that populates. For example if a constraint had a right hand side value of $$\geq$$ 120 and the delta was 20 then \
        optimal decision variables calculate a value of 140 which is 20 within the bound.")
        st.write("")


    example = st.beta_expander("Example Problem", expanded = 0 )
    with example:
        st.write("")
        st.write("**A Simple Development Problem**")
        st.write("Building Co. have purchased 20 acres of land in Coastal New South Wales and are trying to determine \
        which type of homes they should build to maximize gross profit. There are four types of homes they can \
        build (see below table) and Building Co. have decided at least 10 models of each should be constructed. Futhermore \
        at least 40 homes must be one story and at least 50 must have three or more bedrooms.")

        buildingco = {'Model':['Coastal Cabin','Beach Bungalow', 'Tranquil Townhouse', 'Eastern Estate'],
        'Acreage': ['0.20','0.27','0.22','0.35'],
        'Stories':['1','1','2','2'],
        'Bedrooms':['2','3','3','4'],
        'Gross Profit': ['$40,000','$50,000','$60,000','$80,000']}
        buildingdf = pd.DataFrame(buildingco, columns = ['Model','Acreage','Stories','Bedrooms','Gross Profit'])
        building_table = buildingdf.set_index('Model')
        st.table(building_table)
        st.write("Formulate an optimization model to determine Building Co's optimal development plan to \
        maximise gross profit." )
        st.write("**Solution**")
        st.write("Let $$x_i$$ be the number of model i homes developed by Building Co. Where i = 1, 2, 3, 4 \
        corresponds to Coastal Cabin, Beach Bungalow, Tranquil Townhouse and Eastern Estate models respectively.")
        st.write("**Objective function:**")
        st.write("Maximise: 40,000$$x_1$$ + 50,000$$x_2$$ + 60,000$$x_3$$ + 80,000$$x_4$$")
        st.write("**Constraints:**")
        st.write("(1) $$x_i$$  $${\geq}$$  10    $${\\forall} i ,  i = 1,...,4$$")
        st.write("(2) $$x_1 + x_2 {\geq}$$ 40")
        st.write("(3) $$x_2 + x_3 + x_4 {\geq}$$ 50")
        st.write("(4) 0.20$$x_1$$ + 0.27$$x_2$$ + 0.22$$x_3$$ + 0.35$$x_4$$ $${\leq}$$ 20")
        st.write("Note constraints must also be added to ensure non negative and integer variables \
        this can be specified in the *user input* sidebar. ")
        st.write("**Interpretation of constraints:**")
        st.write("Constraint (1) refers to the requirement that at least 10 of each model be built. \
        Constraint (2) requires at least 40 homes be 1 story, Constraint (3) requires at least 50 homes \
        have three or more bedrooms and Constraint (4) ensures the the acreage available isn't exceeded. \
        The requirement for integer non negative variables is needed because \
        Building Co. can't develop a negative number of homes or incomplete homes.")
        st.write("**Solution:**")
        st.write("Optimal value: $4,610,000")
        st.write("$$x_1$$ = 29, $$x_2$$ = 11, $$x_3$$ = 35, $$x_4$$ = 10")
        st.write("**Interpretation of Solution:**")
        st.write("Building Co. should develop 29 Coastal Cabins, 11 Beach Bungalows, 35 Tranquil Townhouses \
        and 10 Eastern Estates. This will maximize gross profit subject to the constraints at $4.61m")


def main():
    #app_mode.sidebar
    st.sidebar.header('User Input Parameters')

    st.sidebar.subheader('**Project Name**')
    name = st.sidebar.text_input("Enter a Project Name")

    st.sidebar.subheader('**Model Sense**')
    Sense = st.sidebar.selectbox('Are you solving a maximization or minimization problem?',('Maximize','Minimize'))

    st.sidebar.subheader('**Variable Name**')
    var_prefix = st.sidebar.text_input("Enter a word to describe the varibales")

    st.sidebar.subheader('**Number of Decision Variables**')
    num_variables = st.sidebar.slider('Select number of variables', min_value=0,max_value=10)

    st.sidebar.subheader('**Number of Constraints**')
    num_constraints = st.sidebar.slider('Select number of constraints', min_value=0,max_value=12)


    show_con = st.sidebar.checkbox('Do you wish to display constraints in the configuration summary?')

    st.sidebar.subheader('**Primary Variable Type**')
    var_type = st.sidebar.selectbox('Select a variable type',('Continuous','Integer'))

    st.sidebar.subheader('**Binary Variables**')
    binary = st.sidebar.selectbox("Do you require any of the variables to be binary?",('No','Yes'))

    st.sidebar.subheader('**Non-Negative Variables**')
    non_neg = st.sidebar.selectbox('Do you wish to enforce a zero lower bound for variables?',('Yes','No'))


    #var_list = ['x1','x2','x3','x4','x5','x6','x7','x8','x9','x10']




    #Main window components

    # Model output
    model_output = st.beta_container()
    optimize_now = model_output.checkbox('Confirm model and run optimization')

    # Model configuration text

    model_config = st.beta_container()
    model_config.write("## Model Configuration Summary ##")
    model_config.write("")
    model_config.write ("### Your objective function is: ###")
    model_config_con = st.beta_container()
    model_config_con.write("### Your constraints are: ###")
    model_config_con.write("")

    #Objective function section

    def obj_one():
        x_one, value_one = st.beta_columns([3,1])
        with x_one:
            global x1_obj
            x1_obj = st.number_input("Enter the coefficient of x1 in the objective function")
        with value_one:
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.write("$x_1$")

    def obj_two():
        x_two, value_two = st.beta_columns([3,1])
        with x_two:
            global x2_obj
            x2_obj = st.number_input("Enter the coefficient of x2 in the objective function")
        with value_two:
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.write("$x_2$")

    def obj_three():
        x_three, value_three = st.beta_columns([3,1])
        with x_three:
            global x3_obj
            x3_obj = st.number_input("Enter the coefficient of x3 in the objective function")
        with value_three:
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.write("$x_3$")

    def obj_four():
        x_four, value_four = st.beta_columns([3,1])
        with x_four:
            global x4_obj
            x4_obj = st.number_input("Enter the coefficient of x4 in the objective function")
        with value_four:
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.write("$x_4$")


    def obj_five():
        x_five, value_five = st.beta_columns([3,1])
        with x_five:
            global x5_obj
            x5_obj = st.number_input("Enter the coefficient of x5 in the objective function")
        with value_five:
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.write("$x_5$")

    def obj_six():
        x_six, value_six = st.beta_columns([3,1])
        with x_six:
            global x6_obj
            x6_obj = st.number_input("Enter the coefficient of x6 in the objective function")
        with value_six:
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.write("$x_6$")

    def obj_seven():
        x_seven, value_seven = st.beta_columns([3,1])
        with x_seven:
            global x7_obj
            x7_obj = st.number_input("Enter the coefficient of x7 in the objective function")
        with value_seven:
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.write("$x_7$")

    def obj_eight():
        x_eight, value_eight = st.beta_columns([3,1])
        with x_eight:
            global x8_obj
            x8_obj = st.number_input("Enter the coefficient of x8 in the objective function")
        with value_eight:
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.write("$x_8$")

    def obj_nine():
        x_nine, value_nine = st.beta_columns([3,1])
        with x_nine:
            global x9_obj
            x9_obj = st.number_input("Enter the coefficient of x9 in the objective function")
        with value_nine:
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.write("$x_9$")

    def obj_ten():
        x_ten, value_ten = st.beta_columns([3,1])
        with x_ten:
            global x10_obj
            x10_obj = st.number_input("Enter the coefficient of x10 in the objective function")
        with value_ten:
            st.markdown("")
            st.markdown("")
            st.markdown("")
            st.write("$x_{10}$")

    if num_variables == 0:
        expand_obj = 0
    else:
        expand_obj = 0 # change value to one if you want boxes to expand automatically
        st.markdown("## **Construct Your Objective Function**")

        if binary == 'Yes':
            bin_var = st.multiselect("Select which variables are required to be binary",[var_list[0],var_list[1],
            var_list[2],var_list[3],var_list[4],var_list[5],var_list[6],var_list[7],var_list[8],var_list[9]])
        obj_function = st.beta_expander("Define the objective function", expanded = expand_obj )
        with obj_function:

            if num_variables == 1:
                obj_one()


            elif num_variables == 2:
                obj_one()
                obj_two()

            elif num_variables == 3:
                obj_one()
                obj_two()
                obj_three()

            elif num_variables ==4:
                obj_one()
                obj_two()
                obj_three()
                obj_four()

            elif num_variables ==5:
                obj_one()
                obj_two()
                obj_three()
                obj_four()
                obj_five()

            elif num_variables ==6:
                obj_one()
                obj_two()
                obj_three()
                obj_four()
                obj_five()
                obj_six()

            elif num_variables ==7:
                obj_one()
                obj_two()
                obj_three()
                obj_four()
                obj_five()
                obj_six()
                obj_seven()

            elif num_variables == 8:
                obj_one()
                obj_two()
                obj_three()
                obj_four()
                obj_five()
                obj_six()
                obj_seven()
                obj_eight()

            elif num_variables ==9:
                obj_one()
                obj_two()
                obj_three()
                obj_four()
                obj_five()
                obj_six()
                obj_seven()
                obj_eight()
                obj_nine()

            elif num_variables ==10:
                obj_one()
                obj_two()
                obj_three()
                obj_four()
                obj_five()
                obj_six()
                obj_seven()
                obj_eight()
                obj_nine()
                obj_ten()


    with model_config:
        if num_variables == 0:
            model_config.write("Please specify the number of decision variables")
        elif num_variables == 1:
            model_config.write("{} $x_1$".format(x1_obj))
        elif num_variables == 2:
            model_config.write("{} $x_1$ + {} $x_2$".format(x1_obj,x2_obj))
        elif num_variables == 3:
            model_config.write("{} $x_1$ + {} $x_2$ + {} $x_3$".format(x1_obj,x2_obj,x3_obj))
        elif num_variables == 4:
            model_config.write("{} $x_1$ + {} $x_2$ + {} $x_3$ + {} $x_4$".format(x1_obj,x2_obj,x3_obj,x4_obj))
        elif num_variables == 5:
            model_config.write("{} $x_1$ + {} $x_2$ + {} $x_3$ + {} $x_4$ + {} $x_5$".format(x1_obj,x2_obj,x3_obj,x4_obj,x5_obj))
        elif num_variables == 6:
            model_config.write("{} $x_1$ + {} $x_2$ + {} $x_3$ + {} $x_4$ + {} $x_5$ + {} $x_6$".format(x1_obj,x2_obj,x3_obj,x4_obj,x5_obj,x6_obj))
        elif num_variables == 7:
            model_config.write("{} $x_1$ + {} $x_2$ + {} $x_3$ + {} $x_4$ + {} $x_5$ + {} $x_6$ + {} $x_7$".
            format(x1_obj,x2_obj,x3_obj,x4_obj,x5_obj,x6_obj,x7_obj))
        elif num_variables == 8:
            model_config.write("{} $x_1$ + {} $x_2$ + {} $x_3$ + {} $x_4$ + {} $x_5$ + {} $x_6$ + {} $x_7$ + {} $x_8$".
            format(x1_obj,x2_obj,x3_obj,x4_obj,x5_obj,x6_obj,x7_obj,x8_obj))
        elif num_variables == 9:
            model_config.write("{} $x_1$ + {} $x_2$ + {} $x_3$ + {} $x_4$ + {} $x_5$ + {} $x_6$ + {} $x_7$ + {} $x_8$ + {} $x_9$".
            format(x1_obj,x2_obj,x3_obj,x4_obj,x5_obj,x6_obj,x7_obj,x8_obj,x9_obj))
        elif num_variables == 10:
            model_config.write("{} $x_1$ + {} $x_2$ + {} $x_3$ + {} $x_4$ + {} $x_5$ + {} $x_6$ + {} $x_7$ + {} $x_8$ + {} $x_9$ + {} $x_{{10}}$".
            format(x1_obj,x2_obj,x3_obj,x4_obj,x5_obj,x6_obj,x7_obj,x8_obj,x9_obj,x10_obj))








    # Gap between objective function and constraints section

    st.write("")
    st.write("")
    st.write("")



    # Constraint section

    def const_one():
        const_one = st.beta_expander("Define Constraint One", expanded = expand_const[0])
        with const_one:
            #ineqaulity selector
            st.markdown('**Constraint One inequality**')
            global con1_inequality
            con1_inequality = st.selectbox('Define the inequality for constraint One',('>=','<='))
            # RHS bound
            st.markdown('**Constraint One Right Hand Side Value**')
            global con1_rhs
            con1_rhs = st.number_input('Enter the right hand side value of constraint One')

            #LHS variables
            st.markdown('**Constraint One Left Hand Side Variables**')
            global var_sel_con1
            var_sel_con1 = st.multiselect("Select which variables to include in constraint One",[var_list[0],var_list[1],
            var_list[2],var_list[3],var_list[4],var_list[5],var_list[6],var_list[7],var_list[8],var_list[9]])
            con1_x1,con1_val1 = st.beta_columns([3,1])
            if 'x1' in var_sel_con1:
                with con1_x1:
                    global gl_x1_c1
                    gl_x1_c1 = st.number_input('x1 coefficient in constraint One')
                with con1_val1:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_1$")

            con1_x2, con1_val2 = st.beta_columns([3,1])
            if 'x2' in var_sel_con1:
                with con1_x2:
                    global gl_x2_c1
                    gl_x2_c1 = st.number_input('x2 coefficient in constraint One')
                with con1_val2:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_2$")

            con1_x3,con1_val3 = st.beta_columns([3,1])
            if 'x3' in var_sel_con1:
                with con1_x3:
                    global gl_x3_c1
                    gl_x3_c1 = st.number_input('x3 coefficient in constraint One')
                with con1_val3:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_3$")

            con1_x4, con1_val4 = st.beta_columns([3,1])
            if 'x4' in var_sel_con1:
                with con1_x4:
                    global gl_x4_c1
                    gl_x4_c1 = st.number_input('x4 coefficient in constraint One')
                with con1_val4:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_4$")

            con1_x5,con1_val5 = st.beta_columns([3,1])
            if 'x5' in var_sel_con1:
                with con1_x5:
                    global gl_x5_c1
                    gl_x5_c1 = st.number_input('x5 coefficient in constraint One')
                with con1_val5:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_5$")

            con1_x6, con1_val6 = st.beta_columns([3,1])
            if 'x6' in var_sel_con1:
                with con1_x6:
                    global gl_x6_c1
                    gl_x6_c1 = st.number_input('x6 coefficient in constraint One')
                with con1_val6:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_6$")

            con1_x7,con1_val7 = st.beta_columns([3,1])
            if 'x7' in var_sel_con1:
                with con1_x7:
                    global gl_x7_c1
                    gl_x7_c1 = st.number_input('x7 coefficient in constraint One')
                with con1_val7:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_7$")

            con1_x8, con1_val8 = st.beta_columns([3,1])
            if 'x8' in var_sel_con1:
                with con1_x8:
                    global gl_x8_c1
                    gl_x8_c1 = st.number_input('x8 coefficient in constraint One')
                with con1_val8:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_8$")

            con1_x9,con1_val9 = st.beta_columns([3,1])
            if 'x9' in var_sel_con1:
                with con1_x9:
                    global gl_x9_c1
                    gl_x9_c1 = st.number_input('x9 coefficient in constraint One')
                with con1_val9:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_9$")

            con1_x10, con1_val10 = st.beta_columns([3,1])
            if 'x10' in var_sel_con1:
                with con1_x10:
                    global gl_x10_c1
                    gl_x10_c1 = st.number_input('x10 coefficient in constraint One')
                with con1_val10:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_{10}$")


    def const_two():
        const_two = st.beta_expander("Define Constraint Two", expanded = expand_const[1])
        with const_two:
            #ineqaulity selector
            st.markdown('**Constraint Two inequality**')
            global con2_inequality
            con2_inequality = st.selectbox('Define the inequality for constraint Two',('>=','<='))
            # RHS bound
            st.markdown('**Constraint Two Right Hand Side Value**')
            global con2_rhs
            con2_rhs = st.number_input('Enter the right hand side value of constraint Two')

            #LHS variables
            st.markdown('**Constraint Two Left Hand Side Variables**')
            global var_sel_con2
            var_sel_con2 = st.multiselect("Select which variables to include in constraint Two",[var_list[0],var_list[1],
            var_list[2],var_list[3],var_list[4],var_list[5],var_list[6],var_list[7],var_list[8],var_list[9]])
            con2_x1,con2_val1 = st.beta_columns([3,1])
            if 'x1' in var_sel_con2:
                with con2_x1:
                    global gl_x1_c2
                    gl_x1_c2 = st.number_input('x1 coefficient in constraint Two')
                with con2_val1:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_1$")

            con2_x2, con2_val2 = st.beta_columns([3,1])
            if 'x2' in var_sel_con2:
                with con2_x2:
                    global gl_x2_c2
                    gl_x2_c2 = st.number_input('x2 coefficient in constraint Two')
                with con2_val2:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_2$")

            con2_x3,con2_val3 = st.beta_columns([3,1])
            if 'x3' in var_sel_con2:
                with con2_x3:
                    global gl_x3_c2
                    gl_x3_c2 = st.number_input('x3 coefficient in constraint Two')
                with con2_val3:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_3$")

            con2_x4, con2_val4 = st.beta_columns([3,1])
            if 'x4' in var_sel_con2:
                with con2_x4:
                    global gl_x4_c2
                    gl_x4_c2 = st.number_input('x4 coefficient in constraint Two')
                with con2_val4:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_4$")

            con2_x5,con2_val5 = st.beta_columns([3,1])
            if 'x5' in var_sel_con2:
                with con2_x5:
                    global gl_x5_c2
                    gl_x5_c2 = st.number_input('x5 coefficient in constraint Two')
                with con2_val5:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_5$")

            con2_x6, con2_val6 = st.beta_columns([3,1])
            if 'x6' in var_sel_con2:
                with con2_x6:
                    global gl_x6_c2
                    gl_x6_c2 = st.number_input('x6 coefficient in constraint Two')
                with con2_val6:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_6$")

            con2_x7,con2_val7 = st.beta_columns([3,1])
            if 'x7' in var_sel_con2:
                with con2_x7:
                    global gl_x7_c2
                    gl_x7_c2= st.number_input('x7 coefficient in constraint Two')
                with con2_val7:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_7$")

            con2_x8, con2_val8 = st.beta_columns([3,1])
            if 'x8' in var_sel_con2:
                with con2_x8:
                    global gl_x8_c2
                    gl_x8_c2 = st.number_input('x8 coefficient in constraint One')
                with con2_val8:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_8$")

            con2_x9,con2_val9 = st.beta_columns([3,1])
            if 'x9' in var_sel_con2:
                with con2_x9:
                    global gl_x9_c2
                    gl_x9_c2 = st.number_input('x9 coefficient in constraint Two')
                with con2_val9:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_9$")

            con2_x10, con2_val10 = st.beta_columns([3,1])
            if 'x10' in var_sel_con2:
                with con2_x10:
                    global gl_x10_c2
                    gl_x10_c2 = st.number_input('x10 coefficient in constraint Two')
                with con2_val10:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_{10}$")


    def const_three():
        const_three = st.beta_expander("Define Constraint Three", expanded = expand_const[2])
        with const_three:
            #ineqaulity selector
            st.markdown('**Constraint Three inequality**')
            global con3_inequality
            con3_inequality = st.selectbox('Define the inequality for constraint Three',('>=','<='))
            # RHS bound
            st.markdown('**Constraint Three Right Hand Side Value**')
            global con3_rhs
            con3_rhs = st.number_input('Enter the right hand side value of constraint Three')

            #LHS variables
            st.markdown('**Constraint Three Left Hand Side Variables**')
            global var_sel_con3
            var_sel_con3 = st.multiselect("Select which variables to include in constraint Three",[var_list[0],var_list[1],
            var_list[2],var_list[3],var_list[4],var_list[5],var_list[6],var_list[7],var_list[8],var_list[9]])
            con3_x1,con3_val1 = st.beta_columns([3,1])
            if 'x1' in var_sel_con3:
                with con3_x1:
                    global gl_x1_c3
                    gl_x1_c3 = st.number_input('x1 coefficient in constraint Three')
                with con3_val1:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_1$")

            con3_x2, con3_val2 = st.beta_columns([3,1])
            if 'x2' in var_sel_con3:
                with con3_x2:
                    global gl_x2_c3
                    gl_x2_c3 = st.number_input('x2 coefficient in constraint Three')
                with con3_val2:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_2$")

            con3_x3,con3_val3 = st.beta_columns([3,1])
            if 'x3' in var_sel_con3:
                with con3_x3:
                    global gl_x3_c3
                    gl_x3_c3 = st.number_input('x3 coefficient in constraint Three')
                with con3_val3:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_3$")

            con3_x4, con3_val4 = st.beta_columns([3,1])
            if 'x4' in var_sel_con3:
                with con3_x4:
                    global gl_x4_c3
                    gl_x4_c3 = st.number_input('x4 coefficient in constraint Three')
                with con3_val4:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_4$")

            con3_x5,con3_val5 = st.beta_columns([3,1])
            if 'x5' in var_sel_con3:
                with con3_x5:
                    global gl_x5_c3
                    gl_x5_c3 = st.number_input('x5 coefficient in constraint Three')
                with con3_val5:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_5$")

            con3_x6, con3_val6 = st.beta_columns([3,1])
            if 'x6' in var_sel_con3:
                with con3_x6:
                    global gl_x6_c3
                    gl_x6_c3 = st.number_input('x6 coefficient in constraint Three')
                with con3_val6:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_6$")

            con3_x7,con3_val7 = st.beta_columns([3,1])
            if 'x7' in var_sel_con3:
                with con3_x7:
                    global gl_x7_c3
                    gl_x7_c3 = st.number_input('x7 coefficient in constraint Three')
                with con3_val7:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_7$")

            con3_x8, con3_val8 = st.beta_columns([3,1])
            if 'x8' in var_sel_con3:
                with con3_x8:
                    global gl_x8_c3
                    gl_x8_c3 = st.number_input('x8 coefficient in constraint Three')
                with con3_val8:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_8$")

            con3_x9,con3_val9 = st.beta_columns([3,1])
            if 'x9' in var_sel_con3:
                with con3_x9:
                    global gl_x9_c3
                    gl_x9_c3 = st.number_input('x9 coefficient in constraint Three')
                with con3_val9:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_9$")

            con3_x10, con3_val10 = st.beta_columns([3,1])
            if 'x10' in var_sel_con3:
                with con3_x10:
                    global gl_x10_c3
                    gl_x10_c3 = st.number_input('x10 coefficient in constraint Three')
                with con3_val10:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_{10}$")


    def const_four():
        const_four = st.beta_expander("Define Constraint Four", expanded = expand_const[3])
        with const_four:
            #ineqaulity selector
            st.markdown('**Constraint Four inequality**')
            global con4_inequality
            con4_inequality = st.selectbox('Define the inequality for constraint Four',('>=','<='))
            # RHS bound
            st.markdown('**Constraint Four Right Hand Side Value**')
            global con4_rhs
            con4_rhs = st.number_input('Enter the right hand side value of constraint Four')

            #LHS variables
            st.markdown('**Constraint Three Left Hand Side Variables**')
            global var_sel_con4
            var_sel_con4 = st.multiselect("Select which variables to include in constraint Four",[var_list[0],var_list[1],
            var_list[2],var_list[3],var_list[4],var_list[5],var_list[6],var_list[7],var_list[8],var_list[9]])
            con4_x1,con4_val1 = st.beta_columns([3,1])
            if 'x1' in var_sel_con4:
                with con4_x1:
                    global gl_x1_c4
                    gl_x1_c4 = st.number_input('x1 coefficient in constraint Four')
                with con4_val1:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_1$")

            con4_x2, con4_val2 = st.beta_columns([3,1])
            if 'x2' in var_sel_con4:
                with con4_x2:
                    global gl_x2_c4
                    gl_x2_c4 = st.number_input('x2 coefficient in constraint Four')
                with con4_val2:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_2$")

            con4_x3,con4_val3 = st.beta_columns([3,1])
            if 'x3' in var_sel_con4:
                with con4_x3:
                    global gl_x3_c4
                    gl_x3_c4 = st.number_input('x3 coefficient in constraint Four')
                with con4_val3:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_3$")

            con4_x4, con4_val4 = st.beta_columns([3,1])
            if 'x4' in var_sel_con4:
                with con4_x4:
                    global gl_x4_c4
                    gl_x4_c4 = st.number_input('x4 coefficient in constraint Four')
                with con4_val4:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_4$")

            con4_x5,con4_val5 = st.beta_columns([3,1])
            if 'x5' in var_sel_con4:
                with con4_x5:
                    global gl_x5_c4
                    gl_x5_c4 = st.number_input('x5 coefficient in constraint Four')
                with con4_val5:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_5$")

            con4_x6, con4_val6 = st.beta_columns([3,1])
            if 'x6' in var_sel_con4:
                with con4_x6:
                    global gl_x6_c4
                    gl_x6_c4 = st.number_input('x6 coefficient in constraint Four')
                with con4_val6:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_6$")

            con4_x7,con4_val7 = st.beta_columns([3,1])
            if 'x7' in var_sel_con4:
                with con4_x7:
                    global gl_x7_c4
                    gl_x7_c4= st.number_input('x7 coefficient in constraint Four')
                with con4_val7:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_7$")

            con4_x8, con4_val8 = st.beta_columns([3,1])
            if 'x8' in var_sel_con4:
                with con4_x8:
                    global gl_x8_c4
                    gl_x8_c4 = st.number_input('x8 coefficient in constraint Four')
                with con4_val8:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_8$")

            con4_x9,con4_val9 = st.beta_columns([3,1])
            if 'x9' in var_sel_con4:
                with con4_x9:
                    global gl_x9_c4
                    gl_x9_c4 = st.number_input('x9 coefficient in constraint Four')
                with con4_val9:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_9$")

            con4_x10, con4_val10 = st.beta_columns([3,1])
            if 'x10' in var_sel_con4:
                with con4_x10:
                    global gl_x10_c4
                    gl_x10_c4 = st.number_input('x10 coefficient in constraint Four')
                with con4_val10:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_{10}$")


    def const_five():
        const_five = st.beta_expander("Define Constraint Five", expanded = expand_const[4])
        with const_five:
            #ineqaulity selector
            st.markdown('**Constraint Five inequality**')
            global con5_inequality
            con5_inequality = st.selectbox('Define the inequality for constraint Five',('>=','<='))
            # RHS bound
            st.markdown('**Constraint Five Right Hand Side Value**')
            global con5_rhs
            con5_rhs = st.number_input('Enter the right hand side value of constraint Five')

            #LHS variables
            st.markdown('**Constraint Five Left Hand Side Variables**')
            global var_sel_con5
            var_sel_con5 = st.multiselect("Select which variables to include in constraint Five",[var_list[0],var_list[1],
            var_list[2],var_list[3],var_list[4],var_list[5],var_list[6],var_list[7],var_list[8],var_list[9]])
            con5_x1,con5_val1 = st.beta_columns([3,1])
            if 'x1' in var_sel_con5:
                with con5_x1:
                    global gl_x1_c5
                    gl_x1_c5 = st.number_input('x1 coefficient in constraint Five')
                with con5_val1:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_1$")

            con5_x2, con5_val2 = st.beta_columns([3,1])
            if 'x2' in var_sel_con5:
                with con5_x2:
                    global gl_x2_c5
                    gl_x2_c5 = st.number_input('x2 coefficient in constraint Five')
                with con5_val2:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_2$")

            con5_x3,con5_val3 = st.beta_columns([3,1])
            if 'x3' in var_sel_con5:
                with con5_x3:
                    global gl_x3_c5
                    gl_x3_c5 = st.number_input('x3 coefficient in constraint Five')
                with con5_val3:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_3$")

            con5_x4, con5_val4 = st.beta_columns([3,1])
            if 'x4' in var_sel_con5:
                with con5_x4:
                    global gl_x4_c5
                    gl_x4_c5 = st.number_input('x4 coefficient in constraint Five')
                with con5_val4:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_4$")

            con5_x5,con5_val5 = st.beta_columns([3,1])
            if 'x5' in var_sel_con5:
                with con5_x5:
                    global gl_x5_c5
                    gl_x5_c5 = st.number_input('x5 coefficient in constraint Five')
                with con5_val5:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_5$")

            con5_x6, con5_val6 = st.beta_columns([3,1])
            if 'x6' in var_sel_con5:
                with con5_x6:
                    global gl_x6_c5
                    gl_x6_c5 = st.number_input('x6 coefficient in constraint Five')
                with con5_val6:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_6$")

            con5_x7,con5_val7 = st.beta_columns([3,1])
            if 'x7' in var_sel_con5:
                with con5_x7:
                    global gl_x7_c5
                    gl_x7_c5 = st.number_input('x7 coefficient in constraint Five')
                with con5_val7:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_7$")

            con5_x8, con5_val8 = st.beta_columns([3,1])
            if 'x8' in var_sel_con5:
                with con5_x8:
                    global gl_x8_c5
                    gl_x8_c5 = st.number_input('x8 coefficient in constraint Five')
                with con5_val8:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_8$")

            con5_x9,con5_val9 = st.beta_columns([3,1])
            if 'x9' in var_sel_con5:
                with con5_x9:
                    global gl_x9_c5
                    gl_x9_c5 = st.number_input('x9 coefficient in constraint Five')
                with con5_val9:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_9$")

            con5_x10, con5_val10 = st.beta_columns([3,1])
            if 'x10' in var_sel_con5:
                with con5_x10:
                    global gl_x10_c5
                    gl_x10_c5 = st.number_input('x10 coefficient in constraint Five')
                with con5_val10:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_{10}$")


    def const_six():
        const_six = st.beta_expander("Define Constraint Six", expanded = expand_const[5])
        with const_six:
            #ineqaulity selector
            st.markdown('**Constraint Six inequality**')
            global con6_inequality
            con6_inequality = st.selectbox('Define the inequality for constraint Six',('>=','<='))
            # RHS bound
            st.markdown('**Constraint Six Right Hand Side Value**')
            global con6_rhs
            con6_rhs = st.number_input('Enter the right hand side value of constraint Six')

            #LHS variables
            st.markdown('**Constraint Six Left Hand Side Variables**')
            global var_sel_con6
            var_sel_con6 = st.multiselect("Select which variables to include in constraint Six",[var_list[0],var_list[1],
            var_list[2],var_list[3],var_list[4],var_list[5],var_list[6],var_list[7],var_list[8],var_list[9]])
            con6_x1,con6_val1 = st.beta_columns([3,1])
            if 'x1' in var_sel_con6:
                with con6_x1:
                    global gl_x1_c6
                    gl_x1_c6 = st.number_input('x1 coefficient in constraint Six')
                with con6_val1:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_1$")

            con6_x2, con6_val2 = st.beta_columns([3,1])
            if 'x2' in var_sel_con6:
                with con6_x2:
                    global gl_x2_c6
                    gl_x2_c6 = st.number_input('x2 coefficient in constraint Six')
                with con6_val2:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_2$")

            con6_x3,con6_val3 = st.beta_columns([3,1])
            if 'x3' in var_sel_con6:
                with con6_x3:
                    global gl_x3_c6
                    gl_x3_c6 = st.number_input('x3 coefficient in constraint Six')
                with con6_val3:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_3$")

            con6_x4, con6_val4 = st.beta_columns([3,1])
            if 'x4' in var_sel_con6:
                with con6_x4:
                    global gl_x4_c6
                    gl_x4_c6 = st.number_input('x4 coefficient in constraint Six')
                with con6_val4:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_4$")

            con6_x5,con6_val5 = st.beta_columns([3,1])
            if 'x5' in var_sel_con6:
                with con6_x5:
                    global gl_x5_c6
                    gl_x5_c6 = st.number_input('x5 coefficient in constraint Six')
                with con6_val5:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_5$")

            con6_x6, con6_val6 = st.beta_columns([3,1])
            if 'x6' in var_sel_con6:
                with con6_x6:
                    global gl_x6_c6
                    gl_x6_c6 = st.number_input('x6 coefficient in constraint Six')
                with con6_val6:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_6$")

            con6_x7,con6_val7 = st.beta_columns([3,1])
            if 'x7' in var_sel_con6:
                with con6_x7:
                    global gl_x7_c6
                    gl_x7_c6 = st.number_input('x7 coefficient in constraint Six')
                with con6_val7:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_7$")

            con6_x8, con6_val8 = st.beta_columns([3,1])
            if 'x8' in var_sel_con6:
                with con6_x8:
                    global gl_x8_c6
                    gl_x8_c6 = st.number_input('x8 coefficient in constraint Six')
                with con6_val8:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_8$")

            con6_x9,con6_val9 = st.beta_columns([3,1])
            if 'x9' in var_sel_con6:
                with con6_x9:
                    global gl_x9_c6
                    gl_x9_c6 = st.number_input('x9 coefficient in constraint Six')
                with con6_val9:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_9$")

            con6_x10, con6_val10 = st.beta_columns([3,1])
            if 'x10' in var_sel_con6:
                with con6_x10:
                    global gl_x10_c6
                    gl_x10_c6 = st.number_input('x10 coefficient in constraint Six')
                with con6_val10:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_{10}$")


    def const_seven():
        const_seven = st.beta_expander("Define Constraint Seven", expanded = expand_const[6])
        with const_seven:
            #ineqaulity selector
            st.markdown('**Constraint Seven inequality**')
            global con7_inequality
            con7_inequality = st.selectbox('Define the inequality for constraint Seven',('>=','<='))
            # RHS bound
            st.markdown('**Constraint Seven Right Hand Side Value**')
            global con7_rhs
            con7_rhs = st.number_input('Enter the right hand side value of constraint Seven')

            #LHS variables
            st.markdown('**Constraint Seven Left Hand Side Variables**')
            global var_sel_con7
            var_sel_con7 = st.multiselect("Select which variables to include in constraint Seven",[var_list[0],var_list[1],
            var_list[2],var_list[3],var_list[4],var_list[5],var_list[6],var_list[7],var_list[8],var_list[9]])
            con7_x1,con7_val1 = st.beta_columns([3,1])
            if 'x1' in var_sel_con7:
                with con7_x1:
                    global gl_x1_c7
                    gl_x1_c7 = st.number_input('x1 coefficient in constraint Seven')
                with con7_val1:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_1$")

            con7_x2, con7_val2 = st.beta_columns([3,1])
            if 'x2' in var_sel_con7:
                with con7_x2:
                    global gl_x2_c7
                    gl_x2_c7 = st.number_input('x2 coefficient in constraint Seven')
                with con7_val2:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_2$")

            con7_x3,con7_val3 = st.beta_columns([3,1])
            if 'x3' in var_sel_con7:
                with con7_x3:
                    global gl_x3_c7
                    gl_x3_c7 = st.number_input('x3 coefficient in constraint Seven')
                with con7_val3:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_3$")

            con7_x4, con7_val4 = st.beta_columns([3,1])
            if 'x4' in var_sel_con7:
                with con7_x4:
                    global gl_x4_c7
                    gl_x4_c7 = st.number_input('x4 coefficient in constraint Seven')
                with con7_val4:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_4$")

            con7_x5,con7_val5 = st.beta_columns([3,1])
            if 'x5' in var_sel_con7:
                with con7_x5:
                    global gl_x5_c7
                    gl_x5_c7 = st.number_input('x5 coefficient in constraint Seven')
                with con7_val5:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_5$")

            con7_x6, con7_val6 = st.beta_columns([3,1])
            if 'x6' in var_sel_con7:
                with con7_x6:
                    global gl_x6_c7
                    gl_x6_c7 = st.number_input('x6 coefficient in constraint Seven')
                with con7_val6:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_6$")

            con7_x7,con7_val7 = st.beta_columns([3,1])
            if 'x7' in var_sel_con7:
                with con7_x7:
                    global gl_x7_c7
                    gl_x7_c7 = st.number_input('x7 coefficient in constraint Seven')
                with con7_val7:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_7$")

            con7_x8, con7_val8 = st.beta_columns([3,1])
            if 'x8' in var_sel_con7:
                with con7_x8:
                    global gl_x8_c7
                    gl_x8_c7 = st.number_input('x8 coefficient in constraint Seven')
                with con7_val8:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_8$")

            con7_x9,con7_val9 = st.beta_columns([3,1])
            if 'x9' in var_sel_con7:
                with con7_x9:
                    global gl_x9_c7
                    gl_x9_c7 = st.number_input('x9 coefficient in constraint Seven')
                with con7_val9:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_9$")

            con7_x10, con7_val10 = st.beta_columns([3,1])
            if 'x10' in var_sel_con7:
                with con7_x10:
                    global gl_x10_c7
                    gl_x10_c7 = st.number_input('x10 coefficient in constraint Seven')
                with con7_val10:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_{10}$")


    def const_eight():
        const_eight = st.beta_expander("Define Constraint Eight", expanded = expand_const[7])
        with const_eight:
            #ineqaulity selector
            st.markdown('**Constraint Eight inequality**')
            global con8_inequality
            con8_inequality = st.selectbox('Define the inequality for constraint Eight',('>=','<='))
            # RHS bound
            st.markdown('**Constraint Eight Right Hand Side Value**')
            global con8_rhs
            con8_rhs = st.number_input('Enter the right hand side value of constraint Eight')

            #LHS variables
            st.markdown('**Constraint Eight Left Hand Side Variables**')
            global var_sel_con8
            var_sel_con8 = st.multiselect("Select which variables to include in constraint Eight",[var_list[0],var_list[1],
            var_list[2],var_list[3],var_list[4],var_list[5],var_list[6],var_list[7],var_list[8],var_list[9]])
            con8_x1,con8_val1 = st.beta_columns([3,1])
            if 'x1' in var_sel_con8:
                with con8_x1:
                    global gl_x1_c8
                    gl_x1_c8 = st.number_input('x1 coefficient in constraint Eight')
                with con8_val1:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_1$")

            con8_x2, con8_val2 = st.beta_columns([3,1])
            if 'x2' in var_sel_con8:
                with con8_x2:
                    global gl_x2_c8
                    gl_x2_c8 = st.number_input('x2 coefficient in constraint Eight')
                with con8_val2:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_2$")

            con8_x3,con8_val3 = st.beta_columns([3,1])
            if 'x3' in var_sel_con8:
                with con8_x3:
                    global gl_x3_c8
                    gl_x3_c8 = st.number_input('x3 coefficient in constraint Eight')
                with con8_val3:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_3$")

            con8_x4, con8_val4 = st.beta_columns([3,1])
            if 'x4' in var_sel_con8:
                with con8_x4:
                    global gl_x4_c8
                    gl_x4_c8 = st.number_input('x4 coefficient in constraint Eight')
                with con8_val4:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_4$")

            con8_x5,con8_val5 = st.beta_columns([3,1])
            if 'x5' in var_sel_con8:
                with con8_x5:
                    global gl_x5_c8
                    gl_x5_c8 = st.number_input('x5 coefficient in constraint Eight')
                with con8_val5:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_5$")

            con8_x6, con8_val6 = st.beta_columns([3,1])
            if 'x6' in var_sel_con8:
                with con8_x6:
                    global gl_x6_c8
                    gl_x6_c8 = st.number_input('x6 coefficient in constraint Eight')
                with con8_val6:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_6$")

            con8_x7,con8_val7 = st.beta_columns([3,1])
            if 'x7' in var_sel_con8:
                with con8_x7:
                    global gl_x7_c8
                    gl_x7_c8 = st.number_input('x7 coefficient in constraint Eight')
                with con8_val7:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_7$")

            con8_x8, con8_val8 = st.beta_columns([3,1])
            if 'x8' in var_sel_con8:
                with con8_x8:
                    global gl_x8_c8
                    gl_x8_c8 = st.number_input('x8 coefficient in constraint Eight')
                with con8_val8:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_8$")

            con8_x9,con8_val9 = st.beta_columns([3,1])
            if 'x9' in var_sel_con8:
                with con8_x9:
                    global gl_x9_c8
                    gl_x9_c8 = st.number_input('x9 coefficient in constraint Eight')
                with con8_val9:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_9$")

            con8_x10, con8_val10 = st.beta_columns([3,1])
            if 'x10' in var_sel_con8:
                with con8_x10:
                    global gl_x10_c8
                    gl_x10_c8 = st.number_input('x10 coefficient in constraint Eight')
                with con8_val10:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_{10}$")


    def const_nine():
        const_nine = st.beta_expander("Define Constraint Nine", expanded = expand_const[8])
        with const_nine:
            #ineqaulity selector
            st.markdown('**Constraint Nine inequality**')
            global con9_inequality
            con9_inequality = st.selectbox('Define the inequality for constraint Nine',('>=','<='))
            # RHS bound
            st.markdown('**Constraint Nine Right Hand Side Value**')
            global con9_rhs
            con9_rhs = st.number_input('Enter the right hand side value of constraint Nine')

            #LHS variables
            st.markdown('**Constraint Nine Left Hand Side Variables**')
            global var_sel_con9
            var_sel_con9 = st.multiselect("Select which variables to include in constraint Nine",[var_list[0],var_list[1],
            var_list[2],var_list[3],var_list[4],var_list[5],var_list[6],var_list[7],var_list[8],var_list[9]])
            con9_x1,con9_val1 = st.beta_columns([3,1])
            if 'x1' in var_sel_con9:
                with con9_x1:
                    global gl_x1_c9
                    gl_x1_c9 = st.number_input('x1 coefficient in constraint Nine')
                with con9_val1:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_1$")

            con9_x2, con9_val2 = st.beta_columns([3,1])
            if 'x2' in var_sel_con9:
                with con9_x2:
                    global gl_x2_c9
                    gl_x2_c9 = st.number_input('x2 coefficient in constraint Nine')
                with con9_val2:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_2$")

            con9_x3,con9_val3 = st.beta_columns([3,1])
            if 'x3' in var_sel_con9:
                with con9_x3:
                    global gl_x3_c9
                    gl_x3_c9 = st.number_input('x3 coefficient in constraint Nine')
                with con9_val3:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_3$")

            con9_x4, con9_val4 = st.beta_columns([3,1])
            if 'x4' in var_sel_con9:
                with con9_x4:
                    global gl_x4_c9
                    gl_x4_c9 = st.number_input('x4 coefficient in constraint Nine')
                with con9_val4:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_4$")

            con9_x5,con9_val5 = st.beta_columns([3,1])
            if 'x5' in var_sel_con9:
                with con9_x5:
                    global gl_x5_c9
                    gl_x5_c9 = st.number_input('x5 coefficient in constraint Nine')
                with con9_val5:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_5$")

            con9_x6, con9_val6 = st.beta_columns([3,1])
            if 'x6' in var_sel_con9:
                with con9_x6:
                    global gl_x6_c9
                    gl_x6_c9 = st.number_input('x6 coefficient in constraint Nine')
                with con9_val6:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_6$")

            con9_x7,con9_val7 = st.beta_columns([3,1])
            if 'x7' in var_sel_con9:
                with con9_x7:
                    global gl_x7_c9
                    gl_x7_c9 = st.number_input('x7 coefficient in constraint Nine')
                with con9_val7:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_7$")

            con9_x8, con9_val8 = st.beta_columns([3,1])
            if 'x8' in var_sel_con9:
                with con9_x8:
                    global gl_x8_c9
                    gl_x8_c9 = st.number_input('x8 coefficient in constraint Nine')
                with con9_val8:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_8$")

            con9_x9,con9_val9 = st.beta_columns([3,1])
            if 'x9' in var_sel_con9:
                with con9_x9:
                    global gl_x9_c9
                    gl_x9_c9 = st.number_input('x9 coefficient in constraint Nine')
                with con9_val9:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_9$")

            con9_x10, con9_val10 = st.beta_columns([3,1])
            if 'x10' in var_sel_con9:
                with con9_x10:
                    global gl_x10_c9
                    gl_x10_c9 = st.number_input('x10 coefficient in constraint Nine')
                with con9_val10:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_{10}$")


    def const_ten():
        const_ten = st.beta_expander("Define Constraint Ten", expanded = expand_const[9])
        with const_ten:
            #ineqaulity selector
            st.markdown('**Constraint Ten inequality**')
            global con10_inequality
            con10_inequality = st.selectbox('Define the inequality for constraint Ten',('>=','<='))
            # RHS bound
            st.markdown('**Constraint Ten Right Hand Side Value**')
            global con10_rhs
            con10_rhs = st.number_input('Enter the right hand side value of constraint Ten')

            #LHS variables
            st.markdown('**Constraint Ten Left Hand Side Variables**')
            global var_sel_con10
            var_sel_con10 = st.multiselect("Select which variables to include in constraint Ten",[var_list[0],var_list[1],
            var_list[2],var_list[3],var_list[4],var_list[5],var_list[6],var_list[7],var_list[8],var_list[9]])
            con10_x1,con10_val1 = st.beta_columns([3,1])
            if 'x1' in var_sel_con10:
                with con10_x1:
                    global gl_x1_c10
                    gl_x1_c10 = st.number_input('x1 coefficient in constraint Ten')
                with con10_val1:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_1$")

            con10_x2, con10_val2 = st.beta_columns([3,1])
            if 'x2' in var_sel_con10:
                with con10_x2:
                    global gl_x2_c10
                    gl_x2_c10 = st.number_input('x2 coefficient in constraint Ten')
                with con10_val2:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_2$")

            con10_x3,con10_val3 = st.beta_columns([3,1])
            if 'x3' in var_sel_con10:
                with con10_x3:
                    global gl_x3_c10
                    gl_x3_c10 = st.number_input('x3 coefficient in constraint Ten')
                with con10_val3:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_3$")

            con10_x4, con10_val4 = st.beta_columns([3,1])
            if 'x4' in var_sel_con10:
                with con10_x4:
                    global gl_x4_c10
                    gl_x4_c10 = st.number_input('x4 coefficient in constraint Ten')
                with con10_val4:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_4$")

            con10_x5,con10_val5 = st.beta_columns([3,1])
            if 'x5' in var_sel_con10:
                with con10_x5:
                    global gl_x5_c10
                    gl_x5_c10 = st.number_input('x5 coefficient in constraint Ten')
                with con10_val5:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_5$")

            con10_x6, con10_val6 = st.beta_columns([3,1])
            if 'x6' in var_sel_con10:
                with con10_x6:
                    global gl_x6_c10
                    gl_x6_c10 = st.number_input('x6 coefficient in constraint Ten')
                with con10_val6:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_6$")

            con10_x7,con10_val7 = st.beta_columns([3,1])
            if 'x7' in var_sel_con10:
                with con10_x7:
                    global gl_x7_c10
                    gl_x7_c10 = st.number_input('x7 coefficient in constraint Ten')
                with con10_val7:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_7$")

            con10_x8, con10_val8 = st.beta_columns([3,1])
            if 'x8' in var_sel_con10:
                with con10_x8:
                    global gl_x8_c10
                    gl_x8_c10 = st.number_input('x8 coefficient in constraint Ten')
                with con10_val8:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_8$")

            con10_x9,con10_val9 = st.beta_columns([3,1])
            if 'x9' in var_sel_con10:
                with con10_x9:
                    global gl_x9_c10
                    gl_x9_c10 = st.number_input('x9 coefficient in constraint Ten')
                with con10_val9:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_9$")

            con10_x10, con10_val10 = st.beta_columns([3,1])
            if 'x10' in var_sel_con10:
                with con10_x10:
                    global gl_x10_c10
                    gl_x10_c10 = st.number_input('x10 coefficient in constraint Ten')
                with con10_val10:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_{10}$")


    def const_eleven():
        const_eleven = st.beta_expander("Define Constraint Eleven", expanded = expand_const[10])
        with const_eleven:
            #ineqaulity selector
            st.markdown('**Constraint Eleven inequality**')
            global con11_inequality
            con11_inequality = st.selectbox('Define the inequality for constraint Eleven',('>=','<='))
            # RHS bound
            st.markdown('**Constraint Eleven Right Hand Side Value**')
            global con11_rhs
            con11_rhs = st.number_input('Enter the right hand side value of constraint Eleven')

            #LHS variables
            st.markdown('**Constraint Eleven Left Hand Side Variables**')
            global var_sel_con11
            var_sel_con11 = st.multiselect("Select which variables to include in constraint Eleven",[var_list[0],var_list[1],
            var_list[2],var_list[3],var_list[4],var_list[5],var_list[6],var_list[7],var_list[8],var_list[9]])
            con11_x1,con11_val1 = st.beta_columns([3,1])
            if 'x1' in var_sel_con11:
                with con11_x1:
                    global gl_x1_c11
                    gl_x1_c11 = st.number_input('x1 coefficient in constraint Eleven')
                with con11_val1:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_1$")

            con11_x2, con11_val2 = st.beta_columns([3,1])
            if 'x2' in var_sel_con11:
                with con11_x2:
                    global gl_x2_c11
                    gl_x2_c11 = st.number_input('x2 coefficient in constraint Eleven')
                with con11_val2:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_2$")

            con11_x3,con11_val3 = st.beta_columns([3,1])
            if 'x3' in var_sel_con11:
                with con11_x3:
                    global gl_x3_c11
                    gl_x3_c11 = st.number_input('x3 coefficient in constraint Eleven')
                with con11_val3:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_3$")

            con11_x4, con11_val4 = st.beta_columns([3,1])
            if 'x4' in var_sel_con11:
                with con11_x4:
                    global gl_x4_c11
                    gl_x4_c11 = st.number_input('x4 coefficient in constraint Eleven')
                with con11_val4:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_4$")

            con11_x5,con11_val5 = st.beta_columns([3,1])
            if 'x5' in var_sel_con11:
                with con11_x5:
                    global gl_x5_c11
                    gl_x5_c11 = st.number_input('x5 coefficient in constraint Eleven')
                with con11_val5:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_5$")

            con11_x6, con11_val6 = st.beta_columns([3,1])
            if 'x6' in var_sel_con11:
                with con11_x6:
                    global gl_x6_c11
                    gl_x6_c11 = st.number_input('x6 coefficient in constraint Eleven')
                with con11_val6:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_6$")

            con11_x7,con11_val7 = st.beta_columns([3,1])
            if 'x7' in var_sel_con11:
                with con11_x7:
                    global gl_x7_c11
                    gl_x7_c11 = st.number_input('x7 coefficient in constraint Eleven')
                with con11_val7:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_7$")

            con11_x8, con11_val8 = st.beta_columns([3,1])
            if 'x8' in var_sel_con11:
                with con11_x8:
                    global gl_x8_c11
                    gl_x8_c11 = st.number_input('x8 coefficient in constraint Eleven')
                with con11_val8:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_8$")

            con11_x9,con11_val9 = st.beta_columns([3,1])
            if 'x9' in var_sel_con11:
                with con11_x9:
                    global gl_x9_c11
                    gl_x9_c11 = st.number_input('x9 coefficient in constraint Eleven')
                with con11_val9:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_9$")

            con11_x10, con11_val10 = st.beta_columns([3,1])
            if 'x10' in var_sel_con11:
                with con11_x10:
                    global gl_x10_c11
                    gl_x10_c11 = st.number_input('x10 coefficient in constraint Eleven')
                with con11_val10:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_{10}$")


    def const_twelve():
        const_twelve = st.beta_expander("Define Constraint Twelve", expanded = expand_const[11])
        with const_twelve:
            #ineqaulity selector
            st.markdown('**Constraint Twelve inequality**')
            global con12_inequality
            con12_inequality = st.selectbox('Define the inequality for constraint Twelve',('>=','<='))
            # RHS bound
            st.markdown('**Constraint Twelve Right Hand Side Value**')
            global con12_rhs
            con12_rhs = st.number_input('Enter the right hand side value of constraint Twelve')

            #LHS variables
            st.markdown('**Constraint Twelve Left Hand Side Variables**')
            global var_sel_con12
            var_sel_con12 = st.multiselect("Select which variables to include in constraint Twelve",[var_list[0],var_list[1],
            var_list[2],var_list[3],var_list[4],var_list[5],var_list[6],var_list[7],var_list[8],var_list[9]])
            con12_x1,con12_val1 = st.beta_columns([3,1])
            if 'x1' in var_sel_con12:
                with con12_x1:
                    global gl_x1_c12
                    gl_x1_c12 = st.number_input('x1 coefficient in constraint Twelve')
                with con12_val1:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_1$")

            con12_x2, con12_val2 = st.beta_columns([3,1])
            if 'x2' in var_sel_con12:
                with con12_x2:
                    global gl_x2_c12
                    gl_x2_c12 = st.number_input('x2 coefficient in constraint Twelve')
                with con12_val2:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_2$")

            con12_x3,con12_val3 = st.beta_columns([3,1])
            if 'x3' in var_sel_con12:
                with con12_x3:
                    global gl_x3_c12
                    gl_x3_c12 = st.number_input('x3 coefficient in constraint Twelve')
                with con12_val3:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_3$")

            con12_x4, con12_val4 = st.beta_columns([3,1])
            if 'x4' in var_sel_con12:
                with con12_x4:
                    global gl_x4_c12
                    gl_x4_c12 = st.number_input('x4 coefficient in constraint Twelve')
                with con12_val4:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_4$")

            con12_x5,con12_val5 = st.beta_columns([3,1])
            if 'x5' in var_sel_con12:
                with con12_x5:
                    global gl_x5_c12
                    gl_x5_c12 = st.number_input('x5 coefficient in constraint Twelve')
                with con12_val5:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_5$")

            con12_x6, con12_val6 = st.beta_columns([3,1])
            if 'x6' in var_sel_con12:
                with con12_x6:
                    global gl_x6_c12
                    gl_x6_c12 = st.number_input('x6 coefficient in constraint Twelve')
                with con12_val6:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_6$")

            con12_x7,con12_val7 = st.beta_columns([3,1])
            if 'x7' in var_sel_con12:
                with con12_x7:
                    global gl_x7_c12
                    gl_x7_c12 = st.number_input('x7 coefficient in constraint Twelve')
                with con12_val7:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_7$")

            con12_x8, con12_val8 = st.beta_columns([3,1])
            if 'x8' in var_sel_con12:
                with con12_x8:
                    global gl_x8_c12
                    gl_x8_c12 = st.number_input('x8 coefficient in constraint Twelve')
                with con12_val8:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_8$")

            con12_x9,con12_val9 = st.beta_columns([3,1])
            if 'x9' in var_sel_con12:
                with con12_x9:
                    global gl_x9_c12
                    gl_x9_c12 = st.number_input('x9 coefficient in constraint Twelve')
                with con12_val9:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_9$")

            con12_x10, con12_val10 = st.beta_columns([3,1])
            if 'x10' in var_sel_con12:
                with con12_x10:
                    global gl_x10_c12
                    gl_x10_c12 = st.number_input('x10 coefficient in constraint Twelve')
                with con12_val10:
                    st.markdown("")
                    st.markdown("")
                    st.markdown("")
                    st.write("$x_{10}$")



    # change expand cost to all ones if you want boxes to expand automatically
    expand_const = [0,0,0,0,0,0,0,0,0,0,0,0]
    #zero constraints

    if num_constraints != 0:
        st.markdown("## **Construct Your Constraints**")

    if num_constraints == 0:
        expand_const = [0,0,0,0,0,0,0,0,0,0,0,0]

    #one constraint

    elif num_constraints == 1:
        const_one()

    elif num_constraints == 2:
        const_one()
        const_two()

    elif num_constraints == 3:
        const_one()
        const_two()
        const_three()

    elif num_constraints == 4:
        const_one()
        const_two()
        const_three()
        const_four()

    elif num_constraints == 5:
        const_one()
        const_two()
        const_three()
        const_four()
        const_five()

    elif num_constraints == 6:
        const_one()
        const_two()
        const_three()
        const_four()
        const_five()
        const_six()

    elif num_constraints == 7:
        const_one()
        const_two()
        const_three()
        const_four()
        const_five()
        const_six()
        const_seven()

    elif num_constraints == 8:
        const_one()
        const_two()
        const_three()
        const_four()
        const_five()
        const_six()
        const_seven()
        const_eight()

    elif num_constraints == 9:
        const_one()
        const_two()
        const_three()
        const_four()
        const_five()
        const_six()
        const_seven()
        const_eight()
        const_nine()

    elif num_constraints == 10:
        const_one()
        const_two()
        const_three()
        const_four()
        const_five()
        const_six()
        const_seven()
        const_eight()
        const_nine()
        const_ten()

    elif num_constraints == 11:
        const_one()
        const_two()
        const_three()
        const_four()
        const_five()
        const_six()
        const_seven()
        const_eight()
        const_nine()
        const_ten()
        const_eleven()

    elif num_constraints == 12:
        const_one()
        const_two()
        const_three()
        const_four()
        const_five()
        const_six()
        const_seven()
        const_eight()
        const_nine()
        const_ten()
        const_eleven()
        const_twelve()

    #printing a summary of the constraints

    def print_con_one():
        l,c,m = st.beta_columns(3)
        c.write("**Constraint One:**")
        model_config_con.write("#### LHS ####")
        c1,c2,c3,c4,c5 = st.beta_columns(5)
        c6,c7,c8,c9,c10 = st.beta_columns(5)
        model_config_con.write("#### RHS ####")
        if 'x1' in var_sel_con1:
            c1.write("###### {}$x_1$ ######".format(gl_x1_c1))
        if 'x2' in var_sel_con1:
            c2.write("###### $+$ {}$x_2$ ######".format(gl_x2_c1))
        if 'x3' in var_sel_con1:
            c3.write("###### $+$ {}$x_3$ ######".format(gl_x3_c1))
        if 'x4' in var_sel_con1:
            c4.write("###### $+$ {}$x_4$ ######".format(gl_x4_c1))
        if 'x5' in var_sel_con1:
            c5.write("###### $+$ {}$x_5$ ######".format(gl_x5_c1))
        if 'x6' in var_sel_con1:
            c6.write("###### $+$ {}$x_6$ ######".format(gl_x6_c1))
        if 'x7' in var_sel_con1:
            c7.write("###### $+$ {}$x_7$ ######".format(gl_x7_c1))
        if 'x8' in var_sel_con1:
            c8.write("###### $+$ {}$x_8$ ######".format(gl_x8_c1))
        if 'x9' in var_sel_con1:
            c9.write("###### $+$ {}$x_9$ ######".format(gl_x9_c1))
        if 'x10' in var_sel_con1:
            c10.write("###### $+$ {}$x_{{10}}$ ######".format(gl_x10_c1))
        model_config_con.write("###### ${}$ ${}$ ######".format(con1_inequality,con1_rhs))
        model_config_con.write("")

    def print_con_two():
        l,c,m = st.beta_columns(3)
        c.write("**Constraint Two:**")
        model_config_con.write("#### LHS ####")
        c1,c2,c3,c4,c5 = st.beta_columns(5)
        c6,c7,c8,c9,c10 = st.beta_columns(5)
        model_config_con.write("#### RHS ####")
        if 'x1' in var_sel_con2:
            c1.write("###### {}$x_1$ ######".format(gl_x1_c2))
        if 'x2' in var_sel_con2:
            c2.write("###### $+$ {}$x_2$ ######".format(gl_x2_c2))
        if 'x3' in var_sel_con2:
            c3.write("###### $+$ {}$x_3$ ######".format(gl_x3_c2))
        if 'x4' in var_sel_con2:
            c4.write("###### $+$ {}$x_4$ ######".format(gl_x4_c2))
        if 'x5' in var_sel_con2:
            c5.write("###### $+$ {}$x_5$ ######".format(gl_x5_c2))
        if 'x6' in var_sel_con2:
            c6.write("###### $+$ {}$x_6$ ######".format(gl_x6_c2))
        if 'x7' in var_sel_con2:
            c7.write("###### $+$ {}$x_7$ ######".format(gl_x7_c2))
        if 'x8' in var_sel_con2:
            c8.write("###### $+$ {}$x_8$ ######".format(gl_x8_c2))
        if 'x9' in var_sel_con2:
            c9.write("###### $+$ {}$x_9$ ######".format(gl_x9_c2))
        if 'x10' in var_sel_con2:
            c10.write("###### $+$ {}$x_{{10}}$ ######".format(gl_x10_c2))
        model_config_con.write("###### ${}$ ${}$ ######".format(con2_inequality,con2_rhs))
        model_config_con.write("")

    def print_con_three():
        l,c,m = st.beta_columns(3)
        c.write("**Constraint Three:**")
        model_config_con.write("#### LHS ####")
        c1,c2,c3,c4,c5 = st.beta_columns(5)
        c6,c7,c8,c9,c10 = st.beta_columns(5)
        model_config_con.write("#### RHS ####")
        if 'x1' in var_sel_con3:
            c1.write("###### {}$x_1$ ######".format(gl_x1_c3))
        if 'x2' in var_sel_con3:
            c2.write("###### $+$ {}$x_2$ ######".format(gl_x2_c3))
        if 'x3' in var_sel_con3:
            c3.write("###### $+$ {}$x_3$ ######".format(gl_x3_c3))
        if 'x4' in var_sel_con3:
            c4.write("###### $+$ {}$x_4$ ######".format(gl_x4_c3))
        if 'x5' in var_sel_con3:
            c5.write("###### $+$ {}$x_5$ ######".format(gl_x5_c3))
        if 'x6' in var_sel_con3:
            c6.write("###### $+$ {}$x_6$ ######".format(gl_x6_c3))
        if 'x7' in var_sel_con3:
            c7.write("###### $+$ {}$x_7$ ######".format(gl_x7_c3))
        if 'x8' in var_sel_con3:
            c8.write("###### $+$ {}$x_8$ ######".format(gl_x8_c3))
        if 'x9' in var_sel_con3:
            c9.write("###### $+$ {}$x_9$ ######".format(gl_x9_c3))
        if 'x10' in var_sel_con3:
            c10.write("###### $+$ {}$x_{{10}}$ ######".format(gl_x10_c3))
        model_config_con.write("###### ${}$ ${}$ ######".format(con3_inequality,con3_rhs))
        model_config_con.write("")


    def print_con_four():
        l,c,m = st.beta_columns(3)
        c.write("**Constraint Four:**")
        model_config_con.write("#### LHS ####")
        c1,c2,c3,c4,c5 = st.beta_columns(5)
        c6,c7,c8,c9,c10 = st.beta_columns(5)
        model_config_con.write("#### RHS ####")
        if 'x1' in var_sel_con4:
            c1.write("###### {}$x_1$ ######".format(gl_x1_c4))
        if 'x2' in var_sel_con4:
            c2.write("###### $+$ {}$x_2$ ######".format(gl_x2_c4))
        if 'x3' in var_sel_con4:
            c3.write("###### $+$ {}$x_3$ ######".format(gl_x3_c4))
        if 'x4' in var_sel_con4:
            c4.write("###### $+$ {}$x_4$ ######".format(gl_x4_c4))
        if 'x5' in var_sel_con4:
            c5.write("###### $+$ {}$x_5$ ######".format(gl_x5_c4))
        if 'x6' in var_sel_con4:
            c6.write("###### $+$ {}$x_6$ ######".format(gl_x6_c4))
        if 'x7' in var_sel_con4:
            c7.write("###### $+$ {}$x_7$ ######".format(gl_x7_c4))
        if 'x8' in var_sel_con4:
            c8.write("###### $+$ {}$x_8$ ######".format(gl_x8_c4))
        if 'x9' in var_sel_con4:
            c9.write("###### $+$ {}$x_9$ ######".format(gl_x9_c4))
        if 'x10' in var_sel_con4:
            c10.write("###### $+$ {}$x_{{10}}$ ######".format(gl_x10_c4))
        model_config_con.write("###### ${}$ ${}$ ######".format(con4_inequality,con4_rhs))
        model_config_con.write("")


    def print_con_five():
        l,c,m = st.beta_columns(3)
        c.write("**Constraint Five:**")
        model_config_con.write("#### LHS ####")
        c1,c2,c3,c4,c5 = st.beta_columns(5)
        c6,c7,c8,c9,c10 = st.beta_columns(5)
        model_config_con.write("#### RHS ####")
        if 'x1' in var_sel_con5:
            c1.write("###### {}$x_1$ ######".format(gl_x1_c5))
        if 'x2' in var_sel_con5:
            c2.write("###### $+$ {}$x_2$ ######".format(gl_x2_c5))
        if 'x3' in var_sel_con5:
            c3.write("###### $+$ {}$x_3$ ######".format(gl_x3_c5))
        if 'x4' in var_sel_con5:
            c4.write("###### $+$ {}$x_4$ ######".format(gl_x4_c5))
        if 'x5' in var_sel_con5:
            c5.write("###### $+$ {}$x_5$ ######".format(gl_x5_c5))
        if 'x6' in var_sel_con5:
            c6.write("###### $+$ {}$x_6$ ######".format(gl_x6_c5))
        if 'x7' in var_sel_con5:
            c7.write("###### $+$ {}$x_7$ ######".format(gl_x7_c5))
        if 'x8' in var_sel_con5:
            c8.write("###### $+$ {}$x_8$ ######".format(gl_x8_c5))
        if 'x9' in var_sel_con5:
            c9.write("###### $+$ {}$x_9$ ######".format(gl_x9_c5))
        if 'x10' in var_sel_con5:
            c10.write("###### $+$ {}$x_{{10}}$ ######".format(gl_x10_c5))
        model_config_con.write("###### ${}$ ${}$ ######".format(con5_inequality,con5_rhs))
        model_config_con.write("")


    def print_con_six():
        l,c,m = st.beta_columns(3)
        c.write("**Constraint Six:**")
        model_config_con.write("#### LHS ####")
        c1,c2,c3,c4,c5 = st.beta_columns(5)
        c6,c7,c8,c9,c10 = st.beta_columns(5)
        model_config_con.write("#### RHS ####")
        if 'x1' in var_sel_con6:
            c1.write("###### {}$x_1$ ######".format(gl_x1_c6))
        if 'x2' in var_sel_con6:
            c2.write("###### $+$ {}$x_2$ ######".format(gl_x2_c6))
        if 'x3' in var_sel_con6:
            c3.write("###### $+$ {}$x_3$ ######".format(gl_x3_c6))
        if 'x4' in var_sel_con6:
            c4.write("###### $+$ {}$x_4$ ######".format(gl_x4_c6))
        if 'x5' in var_sel_con6:
            c5.write("###### $+$ {}$x_5$ ######".format(gl_x5_c6))
        if 'x6' in var_sel_con6:
            c6.write("###### $+$ {}$x_6$ ######".format(gl_x6_c6))
        if 'x7' in var_sel_con6:
            c7.write("###### $+$ {}$x_7$ ######".format(gl_x7_c6))
        if 'x8' in var_sel_con6:
            c8.write("###### $+$ {}$x_8$ ######".format(gl_x8_c6))
        if 'x9' in var_sel_con6:
            c9.write("###### $+$ {}$x_9$ ######".format(gl_x9_c6))
        if 'x10' in var_sel_con6:
            c10.write("###### $+$ {}$x_{{10}}$ ######".format(gl_x10_c6))
        model_config_con.write("###### ${}$ ${}$ ######".format(con6_inequality,con6_rhs))
        model_config_con.write("")


    def print_con_seven():
        l,c,m = st.beta_columns(3)
        c.write("**Constraint Seven:**")
        model_config_con.write("#### LHS ####")
        c1,c2,c3,c4,c5 = st.beta_columns(5)
        c6,c7,c8,c9,c10 = st.beta_columns(5)
        model_config_con.write("#### RHS ####")
        if 'x1' in var_sel_con7:
            c1.write("###### {}$x_1$ ######".format(gl_x1_c7))
        if 'x2' in var_sel_con7:
            c2.write("###### $+$ {}$x_2$ ######".format(gl_x2_c7))
        if 'x3' in var_sel_con7:
            c3.write("###### $+$ {}$x_3$ ######".format(gl_x3_c7))
        if 'x4' in var_sel_con7:
            c4.write("###### $+$ {}$x_4$ ######".format(gl_x4_c7))
        if 'x5' in var_sel_con7:
            c5.write("###### $+$ {}$x_5$ ######".format(gl_x5_c7))
        if 'x6' in var_sel_con7:
            c6.write("###### $+$ {}$x_6$ ######".format(gl_x6_c7))
        if 'x7' in var_sel_con7:
            c7.write("###### $+$ {}$x_7$ ######".format(gl_x7_c7))
        if 'x8' in var_sel_con7:
            c8.write("###### $+$ {}$x_8$ ######".format(gl_x8_c7))
        if 'x9' in var_sel_con7:
            c9.write("###### $+$ {}$x_9$ ######".format(gl_x9_c7))
        if 'x10' in var_sel_con7:
            c10.write("###### $+$ {}$x_{{10}}$ ######".format(gl_x10_c7))
        model_config_con.write("###### ${}$ ${}$ ######".format(con7_inequality,con7_rhs))
        model_config_con.write("")


    def print_con_eight():
        l,c,m = st.beta_columns(3)
        c.write("**Constraint Eight:**")
        model_config_con.write("#### LHS ####")
        c1,c2,c3,c4,c5 = st.beta_columns(5)
        c6,c7,c8,c9,c10 = st.beta_columns(5)
        model_config_con.write("#### RHS ####")
        if 'x1' in var_sel_con8:
            c1.write("###### {}$x_1$ ######".format(gl_x1_c8))
        if 'x2' in var_sel_con8:
            c2.write("###### $+$ {}$x_2$ ######".format(gl_x2_c8))
        if 'x3' in var_sel_con8:
            c3.write("###### $+$ {}$x_3$ ######".format(gl_x3_c8))
        if 'x4' in var_sel_con8:
            c4.write("###### $+$ {}$x_4$ ######".format(gl_x4_c8))
        if 'x5' in var_sel_con8:
            c5.write("###### $+$ {}$x_5$ ######".format(gl_x5_c8))
        if 'x6' in var_sel_con8:
            c6.write("###### $+$ {}$x_6$ ######".format(gl_x6_c8))
        if 'x7' in var_sel_con8:
            c7.write("###### $+$ {}$x_7$ ######".format(gl_x7_c8))
        if 'x8' in var_sel_con8:
            c8.write("###### $+$ {}$x_8$ ######".format(gl_x8_c8))
        if 'x9' in var_sel_con8:
            c9.write("###### $+$ {}$x_9$ ######".format(gl_x9_c8))
        if 'x10' in var_sel_con8:
            c10.write("###### $+$ {}$x_{{10}}$ ######".format(gl_x10_c8))
        model_config_con.write("###### ${}$ ${}$ ######".format(con8_inequality,con8_rhs))
        model_config_con.write("")


    def print_con_nine():
        l,c,m = st.beta_columns(3)
        c.write("**Constraint Nine:**")
        model_config_con.write("#### LHS ####")
        c1,c2,c3,c4,c5 = st.beta_columns(5)
        c6,c7,c8,c9,c10 = st.beta_columns(5)
        model_config_con.write("#### RHS ####")
        if 'x1' in var_sel_con9:
            c1.write("###### {}$x_1$ ######".format(gl_x1_c9))
        if 'x2' in var_sel_con9:
            c2.write("###### $+$ {}$x_2$ ######".format(gl_x2_c9))
        if 'x3' in var_sel_con9:
            c3.write("###### $+$ {}$x_3$ ######".format(gl_x3_c9))
        if 'x4' in var_sel_con9:
            c4.write("###### $+$ {}$x_4$ ######".format(gl_x4_c9))
        if 'x5' in var_sel_con9:
            c5.write("###### $+$ {}$x_5$ ######".format(gl_x5_c9))
        if 'x6' in var_sel_con9:
            c6.write("###### $+$ {}$x_6$ ######".format(gl_x6_c9))
        if 'x7' in var_sel_con9:
            c7.write("###### $+$ {}$x_7$ ######".format(gl_x7_c9))
        if 'x8' in var_sel_con9:
            c8.write("###### $+$ {}$x_8$ ######".format(gl_x8_c9))
        if 'x9' in var_sel_con9:
            c9.write("###### $+$ {}$x_9$ ######".format(gl_x9_c9))
        if 'x10' in var_sel_con9:
            c10.write("###### $+$ {}$x_{{10}}$ ######".format(gl_x10_c9))
        model_config_con.write("###### ${}$ ${}$ ######".format(con9_inequality,con9_rhs))
        model_config_con.write("")


    def print_con_ten():
        l,c,m = st.beta_columns(3)
        c.write("**Constraint Ten:**")
        model_config_con.write("#### LHS ####")
        c1,c2,c3,c4,c5 = st.beta_columns(5)
        c6,c7,c8,c9,c10 = st.beta_columns(5)
        model_config_con.write("#### RHS ####")
        if 'x1' in var_sel_con10:
            c1.write("###### {}$x_1$ ######".format(gl_x1_c10))
        if 'x2' in var_sel_con10:
            c2.write("###### $+$ {}$x_2$ ######".format(gl_x2_c10))
        if 'x3' in var_sel_con10:
            c3.write("###### $+$ {}$x_3$ ######".format(gl_x3_c10))
        if 'x4' in var_sel_con10:
            c4.write("###### $+$ {}$x_4$ ######".format(gl_x4_c10))
        if 'x5' in var_sel_con10:
            c5.write("###### $+$ {}$x_5$ ######".format(gl_x5_c10))
        if 'x6' in var_sel_con10:
            c6.write("###### $+$ {}$x_6$ ######".format(gl_x6_c10))
        if 'x7' in var_sel_con10:
            c7.write("###### $+$ {}$x_7$ ######".format(gl_x7_c10))
        if 'x8' in var_sel_con10:
            c8.write("###### $+$ {}$x_8$ ######".format(gl_x8_c10))
        if 'x9' in var_sel_con10:
            c9.write("###### $+$ {}$x_9$ ######".format(gl_x9_c10))
        if 'x10' in var_sel_con10:
            c10.write("###### $+$ {}$x_{{10}}$ ######".format(gl_x10_c10))
        model_config_con.write("###### ${}$ ${}$ ######".format(con10_inequality,con10_rhs))
        model_config_con.write("")


    def print_con_eleven():
        l,c,m = st.beta_columns(3)
        c.write("**Constraint Eleven:**")
        model_config_con.write("#### LHS ####")
        c1,c2,c3,c4,c5 = st.beta_columns(5)
        c6,c7,c8,c9,c10 = st.beta_columns(5)
        model_config_con.write("#### RHS ####")
        if 'x1' in var_sel_con11:
            c1.write("###### {}$x_1$ ######".format(gl_x1_c11))
        if 'x2' in var_sel_con11:
            c2.write("###### $+$ {}$x_2$ ######".format(gl_x2_c11))
        if 'x3' in var_sel_con11:
            c3.write("###### $+$ {}$x_3$ ######".format(gl_x3_c11))
        if 'x4' in var_sel_con11:
            c4.write("###### $+$ {}$x_4$ ######".format(gl_x4_c11))
        if 'x5' in var_sel_con11:
            c5.write("###### $+$ {}$x_5$ ######".format(gl_x5_c11))
        if 'x6' in var_sel_con11:
            c6.write("###### $+$ {}$x_6$ ######".format(gl_x6_c11))
        if 'x7' in var_sel_con11:
            c7.write("###### $+$ {}$x_7$ ######".format(gl_x7_c11))
        if 'x8' in var_sel_con11:
            c8.write("###### $+$ {}$x_8$ ######".format(gl_x8_c11))
        if 'x9' in var_sel_con11:
            c9.write("###### $+$ {}$x_9$ ######".format(gl_x9_c11))
        if 'x10' in var_sel_con11:
            c10.write("###### $+$ {}$x_{{10}}$ ######".format(gl_x10_c11))
        model_config_con.write("###### ${}$ ${}$ ######".format(con11_inequality,con11_rhs))
        model_config_con.write("")


    def print_con_twelve():
        l,c,m = st.beta_columns(3)
        c.write("**Constraint Twelve:**")
        model_config_con.write("#### LHS ####")
        c1,c2,c3,c4,c5 = st.beta_columns(5)
        c6,c7,c8,c9,c10 = st.beta_columns(5)
        model_config_con.write("#### RHS ####")
        if 'x1' in var_sel_con12:
            c1.write("###### {}$x_1$ ######".format(gl_x1_c12))
        if 'x2' in var_sel_con12:
            c2.write("###### $+$ {}$x_2$ ######".format(gl_x2_c12))
        if 'x3' in var_sel_con12:
            c3.write("###### $+$ {}$x_3$ ######".format(gl_x3_c12))
        if 'x4' in var_sel_con12:
            c4.write("###### $+$ {}$x_4$ ######".format(gl_x4_c12))
        if 'x5' in var_sel_con12:
            c5.write("###### $+$ {}$x_5$ ######".format(gl_x5_c12))
        if 'x6' in var_sel_con12:
            c6.write("###### $+$ {}$x_6$ ######".format(gl_x6_c12))
        if 'x7' in var_sel_con12:
            c7.write("###### $+$ {}$x_7$ ######".format(gl_x7_c12))
        if 'x8' in var_sel_con12:
            c8.write("###### $+$ {}$x_8$ ######".format(gl_x8_c12))
        if 'x9' in var_sel_con12:
            c9.write("###### $+$ {}$x_9$ ######".format(gl_x9_c12))
        if 'x10' in var_sel_con12:
            c10.write("###### $+$ {}$x_{{10}}$ ######".format(gl_x10_c12))
        model_config_con.write("###### ${}$ ${}$ ######".format(con12_inequality,con12_rhs))
        model_config_con.write("")

    with model_config_con:
        if show_con == 0:
            model_config_con.write("To display a summary of your constraints check the box in the sidebar")
        if num_constraints == 0 and show_con == 1:
            model_config_con.write("Please specify the number of constraints")
        #if show_con == 1 and optimize_now == 1:
            #model_config_con.write("Configuration summary has been supressed")
        elif num_constraints == 1 and show_con ==1:
            print_con_one()
        elif num_constraints == 2 and show_con ==1:
            print_con_one()
            print_con_two()
        elif num_constraints == 3 and show_con ==1:
            print_con_one()
            print_con_two()
            print_con_three()
        elif num_constraints == 4 and show_con ==1:
            print_con_one()
            print_con_two()
            print_con_three()
            print_con_four()
        elif num_constraints == 5 and show_con ==1:
            print_con_one()
            print_con_two()
            print_con_three()
            print_con_four()
            print_con_five()
        elif num_constraints == 6 and show_con ==1:
            print_con_one()
            print_con_two()
            print_con_three()
            print_con_four()
            print_con_five()
            print_con_six()
        elif num_constraints == 7 and show_con ==1:
            print_con_one()
            print_con_two()
            print_con_three()
            print_con_four()
            print_con_five()
            print_con_six()
            print_con_seven()
        elif num_constraints == 8 and show_con ==1:
            print_con_one()
            print_con_two()
            print_con_three()
            print_con_four()
            print_con_five()
            print_con_six()
            print_con_seven()
            print_con_eight()
        elif num_constraints == 9 and show_con ==1:
            print_con_one()
            print_con_two()
            print_con_three()
            print_con_four()
            print_con_five()
            print_con_six()
            print_con_seven()
            print_con_eight()
            print_con_nine()
        elif num_constraints == 10 and show_con ==1:
            print_con_one()
            print_con_two()
            print_con_three()
            print_con_four()
            print_con_five()
            print_con_six()
            print_con_seven()
            print_con_eight()
            print_con_nine()
            print_con_ten()
        elif num_constraints == 11 and show_con ==1:
            print_con_one()
            print_con_two()
            print_con_three()
            print_con_four()
            print_con_five()
            print_con_six()
            print_con_seven()
            print_con_eight()
            print_con_nine()
            print_con_ten()
            print_con_eleven()
        elif num_constraints == 12 and show_con ==1:
            print_con_one()
            print_con_two()
            print_con_three()
            print_con_four()
            print_con_five()
            print_con_six()
            print_con_seven()
            print_con_eight()
            print_con_nine()
            print_con_ten()
            print_con_eleven()
            print_con_twelve()


    #Optimization code


    #Input data

    #name = name # already defined str

    #var_prefix = var_prefix #already defined str

    #var_list = var_list # already defined list of strings

    varobj = {"x1":x1_obj,"x2":x2_obj,"x3":x3_obj,"x4":x4_obj,"x5":x5_obj,"x6":x6_obj,"x7":x7_obj,"x8":x8_obj,"x9":x9_obj,"x10":x10_obj}

    #var_type = var_type #already defined str

    const_name = ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve"]

    const_bound = [con1_rhs, con2_rhs, con3_rhs, con4_rhs, con5_rhs, con6_rhs, con7_rhs, con8_rhs, con9_rhs, con10_rhs, con11_rhs, con12_rhs]

    lowBound = 0
    if non_neg == 'no':
         lowBound = 10e-20

    sense = LpMaximize
    if Sense == "Minimize":
        sense = LpMinimize



    c1m = [gl_x1_c1, gl_x2_c1, gl_x3_c1, gl_x4_c1, gl_x5_c1, gl_x6_c1, gl_x7_c1, gl_x8_c1, gl_x9_c1, gl_x10_c1]
    inq1 = [1]
    if con1_inequality == "<=":
        inq1 = [-1]

    c2m = [gl_x1_c2, gl_x2_c2, gl_x3_c2, gl_x4_c2, gl_x5_c2, gl_x6_c2, gl_x7_c2, gl_x8_c2, gl_x9_c2, gl_x10_c2]
    inq2 = [1]
    if con2_inequality == "<=":
        inq2 = [-1]

    c3m = [gl_x1_c3, gl_x2_c3, gl_x3_c3, gl_x4_c3, gl_x5_c3, gl_x6_c3, gl_x7_c3, gl_x8_c3, gl_x9_c3, gl_x10_c3]
    inq3 = [1]
    if con3_inequality == "<=":
        inq3 = [-1]

    c4m = [gl_x1_c4, gl_x2_c4, gl_x3_c4, gl_x4_c4, gl_x5_c4, gl_x6_c4, gl_x7_c4, gl_x8_c4, gl_x9_c4, gl_x10_c4]
    inq4 = [1]
    if con4_inequality == "<=":
        inq4 = [-1]

    c5m = [gl_x1_c5, gl_x2_c5, gl_x3_c5, gl_x4_c5, gl_x5_c5, gl_x6_c5, gl_x7_c5, gl_x8_c5, gl_x9_c5, gl_x10_c5]
    inq5 = [1]
    if con5_inequality == "<=":
        inq5 = [-1]

    c6m = [gl_x1_c6, gl_x2_c6, gl_x3_c6, gl_x4_c6, gl_x5_c6, gl_x6_c6, gl_x7_c6, gl_x8_c6, gl_x9_c6, gl_x10_c6]
    inq6 = [1]
    if con6_inequality == "<=":
        inq6 = [-1]



    c7m = [gl_x1_c7, gl_x2_c7, gl_x3_c7, gl_x4_c7, gl_x5_c7, gl_x6_c7, gl_x7_c7, gl_x8_c7, gl_x9_c7, gl_x10_c7]
    inq7 = [1]
    if con7_inequality == "<=":
        inq7 = [-1]



    c8m = [gl_x1_c8, gl_x2_c8, gl_x3_c8, gl_x4_c8, gl_x5_c8, gl_x6_c8, gl_x7_c8, gl_x8_c8, gl_x9_c8, gl_x10_c8]
    inq8 = [1]
    if con8_inequality == "<=":
        inq8 = [-1]



    c9m = [gl_x1_c9, gl_x2_c9, gl_x3_c9, gl_x4_c9, gl_x5_c9, gl_x6_c9, gl_x7_c9, gl_x8_c9, gl_x9_c9, gl_x10_c9]
    inq9 = [1]
    if con9_inequality == "<=":
        inq9 = [-1]



    c10m = [gl_x1_c10, gl_x2_c10, gl_x3_c10, gl_x4_c10, gl_x5_c10, gl_x6_c10, gl_x7_c10, gl_x8_c10, gl_x9_c10, gl_x10_c10]
    inq10 = [1]
    if con10_inequality == "<=":
        inq10 = [-1]



    c11m = [gl_x1_c11, gl_x2_c11, gl_x3_c11, gl_x4_c11, gl_x5_c11, gl_x6_c11, gl_x7_c11, gl_x8_c11, gl_x9_c11, gl_x10_c11]
    inq11 = [1]
    if con11_inequality == "<=":
        inq11 = [-1]



    c12m = [gl_x1_c12, gl_x2_c12, gl_x3_c12, gl_x4_c12, gl_x5_c12, gl_x6_c12, gl_x7_c12, gl_x8_c12, gl_x9_c12, gl_x10_c12]
    inq12 = [1]
    if con12_inequality == "<=":
        inq12 = [-1]

    #make the category list dynamic for binary variables

    cat_list = {"x1":var_type,"x2":var_type, "x3":var_type, "x4":var_type, "x5":var_type,
                "x6":var_type, "x7":var_type, "x8":var_type, "x9":var_type, "x10":var_type}

    up_bound = {"x1":1e32, "x2":1e32, "x3":1e32, "x4":1e32, "x5":1e32,
                "x6":1e32, "x7":1e32, "x8":1e32, "x9":1e32, "x10":1e32}


    if binary == "Yes" and num_variables != 0:
        for i,j in cat_list.items():
            if i in bin_var:
                cat_list[i] = 'Integer'
                up_bound[i] = 1


    #Model data
    model = LpProblem(name = name, sense = sense)
    var = LpVariable.dicts(var_prefix,var_list,lowBound=lowBound, cat=var_type)
    model += lpSum([varobj[i]*var[i] for i in varobj])
    for i,j in varobj.items():
        var[i].cat = cat_list[i]
        var[i].upBound = up_bound[i]

    #Model constraints
    #constraint 1
    model += ((var["x1"]*c1m[0]+var["x2"]*c1m[1]+var["x3"]*c1m[2]+var["x4"]*
              c1m[3]+var["x5"]*c1m[4]+var["x6"]*c1m[5]+var["x7"]*
              c1m[6]+var["x8"]*c1m[7]+var["x9"]*c1m[8])*inq1[0]>=const_bound[0]*inq1[0], const_name[0])
    #constraint 2
    model += ((var["x1"]*c2m[0]+var["x2"]*c2m[1]+var["x3"]*c2m[2]+var["x4"]*
              c2m[3]+var["x5"]*c2m[4]+var["x6"]*c2m[5]+var["x7"]*
              c2m[6]+var["x8"]*c2m[7]+var["x9"]*c2m[8])*inq2[0]>=const_bound[1]*inq2[0], const_name[1])
    #constraint 3
    model += ((var["x1"]*c3m[0]+var["x2"]*c3m[1]+var["x3"]*c3m[2]+var["x4"]*
              c3m[3]+var["x5"]*c3m[4]+var["x6"]*c3m[5]+var["x7"]*
              c3m[6]+var["x8"]*c3m[7]+var["x9"]*c3m[8])*inq3[0]>=const_bound[2]*inq3[0], const_name[2])
    #constraint 4
    model += ((var["x1"]*c4m[0]+var["x2"]*c4m[1]+var["x3"]*c4m[2]+var["x4"]*
              c4m[3]+var["x5"]*c4m[4]+var["x6"]*c4m[5]+var["x7"]*
              c4m[6]+var["x8"]*c4m[7]+var["x9"]*c4m[8])*inq4[0]>=const_bound[3]*inq4[0], const_name[3])
    #constraint 5
    model += ((var["x1"]*c5m[0]+var["x2"]*c5m[1]+var["x3"]*c5m[2]+var["x4"]*
              c5m[3]+var["x5"]*c5m[4]+var["x6"]*c5m[5]+var["x7"]*
              c5m[6]+var["x8"]*c5m[7]+var["x9"]*c5m[8])*inq5[0]>=const_bound[4]*inq5[0], const_name[4])
    #constraint 6
    model += ((var["x1"]*c6m[0]+var["x2"]*c6m[1]+var["x3"]*c6m[2]+var["x4"]*
              c6m[3]+var["x5"]*c6m[4]+var["x6"]*c6m[5]+var["x7"]*
              c6m[6]+var["x8"]*c6m[7]+var["x9"]*c6m[8])*inq6[0]>=const_bound[5]*inq6[0], const_name[5])
    #constraint 7
    model += ((var["x1"]*c7m[0]+var["x2"]*c7m[1]+var["x3"]*c7m[2]+var["x4"]*
              c7m[3]+var["x5"]*c7m[4]+var["x6"]*c7m[5]+var["x7"]*
              c7m[6]+var["x8"]*c7m[7]+var["x9"]*c7m[8])*inq7[0]>=const_bound[6]*inq7[0], const_name[6])
    #constraint 8
    model += ((var["x1"]*c8m[0]+var["x2"]*c8m[1]+var["x3"]*c8m[2]+var["x4"]*
              c8m[3]+var["x5"]*c8m[4]+var["x6"]*c8m[5]+var["x7"]*
              c8m[6]+var["x8"]*c8m[7]+var["x9"]*c8m[8])*inq8[0]>=const_bound[7]*inq8[0], const_name[7])
    #constraint 9
    model += ((var["x1"]*c9m[0]+var["x2"]*c9m[1]+var["x3"]*c9m[2]+var["x4"]*
              c9m[3]+var["x5"]*c9m[4]+var["x6"]*c9m[5]+var["x7"]*
              c9m[6]+var["x8"]*c9m[7]+var["x9"]*c9m[8])*inq9[0]>=const_bound[8]*inq9[0], const_name[8])
    #constraint 10
    model += ((var["x1"]*c10m[0]+var["x2"]*c10m[1]+var["x3"]*c10m[2]+var["x4"]*
              c10m[3]+var["x5"]*c10m[4]+var["x6"]*c10m[5]+var["x7"]*
              c10m[6]+var["x8"]*c10m[7]+var["x9"]*c10m[8])*inq10[0]>=const_bound[9]*inq10[0], const_name[9])
    #constraint 11
    model += ((var["x1"]*c11m[0]+var["x2"]*c11m[1]+var["x3"]*c11m[2]+var["x4"]*
              c11m[3]+var["x5"]*c11m[4]+var["x6"]*c11m[5]+var["x7"]*
              c11m[6]+var["x8"]*c11m[7]+var["x9"]*c11m[8])*inq11[0]>=const_bound[10]*inq11[0], const_name[10])
    #constraint 12
    model += ((var["x1"]*c12m[0]+var["x2"]*c12m[1]+var["x3"]*c12m[2]+var["x4"]*
              c12m[3]+var["x5"]*c12m[4]+var["x6"]*c12m[5]+var["x7"]*
              c12m[6]+var["x8"]*c12m[7]+var["x9"]*c12m[8])*inq12[0]>=const_bound[11]*inq12[0], const_name[11])

    def print_output():
        status = model.solve()
        with model_output:
            st.write("## Model Output ##")
            st.write("")
            st.write(f"**Status:** {LpStatus[model.status]} solution found")
            st.write(f"**Optimised value:** {model.objective.value():,.2f}")



            for var in model.variables():
                st.write(f"**Optimal value of {var.name}:** {var.value():,.2f}")

            st.write("")

            const_details = st.checkbox('Display the non zero deltas to the constraint bounds')

            st.write("")

            st.write("To begin working on a new model, refresh your web page")

            if const_details == 1:
                for name, constraint in model.constraints.items():
                    if constraint.value() != 0:
                        st.write(f"constraint {name} is {constraint.value():,.2f} unit(s) within the bound")


            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")
            st.write("")



    if optimize_now == 1:
        try:
            print_output()
        except TypeError:
            with model_output:
                st.error("Error: Ensure objective and constraints have been defined before optimizing")



if app_mode == "View the instructions and overview":
    instr()
else:
    main()
