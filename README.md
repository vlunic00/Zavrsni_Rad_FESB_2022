## Bachelor Thesis code - FESB 2022

The above code was used as part of my Bachelor thesis in 2022.

It was an idea I came up with, that tested the use of AI in potentially discovering new physics equations/laws etc.

The basic idea behind it was, given values of certian parameters (some relevant to the equation, some not) and the end results, could the model find an equation that would successfully tie those parameters to the result.  
For more simple equations (in the coded example, the equation for the location of a falling body) a linear regression model was used with great effect.  
The results are written in a vector where the values are coeficients who's position in the vector equals the position of the parameter it's tied to.  
The parameter vector is as follows:  
\['1', 'initial_position', 'initial_velocity', 'mass', 'time', 'initial_position^2', 'initial_position initial_velocity', 'initial_position mass', 'initial_position time', 'initial_velocity^2', 'initial_velocity mass', 'initial_velocity time', 'mass^2', 'mass time', 'time^2']

For more complicated ones such as trygonometric equations (in the coded example, the equation for projectile motion fired at an angle) a symbolic regression model was used, again with great success.

## Running the code

The code is written and compiled in Google Colab, therefore I suggest opening it in Colab and running the cells one by one in order to replicate the results.
