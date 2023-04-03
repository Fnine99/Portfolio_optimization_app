This model is made for learning puposes only and should not be used for investment or decision making.

# Portfolio risk management
### An application of Markowitz efficient frontier and modern portfolio theory

## Usage:
    git clone https://github.com/Fnine99/markowitz_eff_frontier-pmgmt
    
    cd Project
        
    python app/main.py


## Content description:

Step 1) 5 years monthly price time series data fetching on the <a href="https://twelvedata.com">Twelve Data API</a>

see <a href="https://github.com/Fnine99/markowitz_eff_frontier-pmgmt/blob/main/app/data.py">app/data.py</a>

Step 2) Various methods on each assets including:
-Monthly prices
-Monthly returns
-Arithmetic mean return
-Geometric mean return
-Monthly returns standard deviation

see <a href="https://github.com/Fnine99/markowitz_eff_frontier-pmgmt/blob/main/app/assets.py">app/assets.py</a>

Step 3) Portfolio construction and Various portfolio methods including:
-Portfolio return
-Porfolio covariance_matrix
-Portfolio variance
-Portfolio standard deviation
-Portfolio correlation matrix
-Portfolio inverse covariance matrix

see <a href="https://github.com/Fnine99/markowitz_eff_frontier-pmgmt/blob/main/app/portfolio.py">app/portfolio.py</a>

Step 4) Portfolio optimization with <a href="https://docs.scipy.org/doc/scipy/tutorial/optimize.html">Scipy algorithms</a> including finding the assets weights which:
-Minimize the portfolio return
-Maximize the portfolio return
-Minimize the portfolio variance
-Maximize the portfolio variance
-Maximize the portfolio Sharpe ratio

see <a href="https://github.com/Fnine99/markowitz_eff_frontier-pmgmt/blob/main/app/frontier.py">app/frontier.py</a>

Step 5) Efficient frontier construction and portfolios modelling including:
-Generate X amout of (1M) of portfolios
-From those generated portfolios locate the assets weights which:
    >Minimize the portfolio variance
    >Maximize the portfolio Sharpe ratio
-Plot step 4 and 5

# Example results

Step 2:
<br/>
<img width="400" alt="" src="https://user-images.githubusercontent.com/97029819/229621780-afae2449-1056-44fa-b882-812eec861714.png">
<br/>
<br/>
<img width="400" alt="" src="https://user-images.githubusercontent.com/97029819/229622439-de3e3598-c1a0-4b00-853d-c3625f53f7a0.png">
<br/>
<br/>
<img width="249" alt="" src="https://user-images.githubusercontent.com/97029819/229622635-98b35520-6c89-41a5-906d-d52ffc1b127f.png">
<br/>
<br/>
<img width="249" alt="" src="https://user-images.githubusercontent.com/97029819/229622656-02133da5-e931-42be-a508-741fc610e582.png">
<br/>
<br/>
<img width="249" alt="" src="https://user-images.githubusercontent.com/97029819/229622670-c18106c8-f783-4385-bdc1-4b4c3945a855.png">
<br/>
<br/>
<img width="280" alt="" src="https://user-images.githubusercontent.com/97029819/229622676-4c516d11-8c44-407d-920d-924df9237305.png">
<br/>
<br/>
<img width="280" alt="" src="https://user-images.githubusercontent.com/97029819/229622694-dd40d579-43c8-40dc-8749-dd5f033d2829.png">
<br/>

Step 3:
Step 4:
Step 5:

