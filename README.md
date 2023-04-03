This model is made for learning puposes only and should not be used for investment or decision making.

# Portfolio risk management
### An application of the Markowitz efficient frontier model and the Modern Portfolio Theory
In this project I implement the almost complete automation of the portfolio optimization and risk using the Markowitz model.

## Usage:
    mkdir <Folder name>

    cd <Folder name>

    git clone https://github.com/Fnine99/markowitz_eff_frontier-pmgmt
    
    python app/main.py


## Content description:

Step 1) 5 years monthly price time series data fetching on the <a href="https://twelvedata.com">Twelve Data API</a>

see <a href="https://github.com/Fnine99/markowitz_eff_frontier-pmgmt/blob/main/app/data.py">app/data.py</a>

Step 2) Various methods on each assets including:<br/>
-Monthly prices<br/>
-Monthly returns<br/>
-Arithmetic mean return<br/>
-Geometric mean return<br/>
-Monthly returns standard deviation<br/>

see <a href="https://github.com/Fnine99/markowitz_eff_frontier-pmgmt/blob/main/app/assets.py">app/assets.py</a>

Step 3) Portfolio construction and Various portfolio methods including:<br/>
-Portfolio return<br/>
-Porfolio covariance_matrix<br/>
-Portfolio variance<br/>
-Portfolio standard deviation<br/>
-Portfolio correlation matrix<br/>
-Portfolio inverse covariance matrix<br/>

see <a href="https://github.com/Fnine99/markowitz_eff_frontier-pmgmt/blob/main/app/portfolio.py">app/portfolio.py</a>

Step 4) Portfolio optimization with <a href="https://docs.scipy.org/doc/scipy/tutorial/optimize.html">Scipy algorithms</a> including finding the assets weights which:<br/>
-Minimize the portfolio return<br/>
-Maximize the portfolio return<br/>
-Minimize the portfolio variance<br/>
-Maximize the portfolio variance<br/>
-Maximize the portfolio Sharpe ratio<br/>

see <a href="https://github.com/Fnine99/markowitz_eff_frontier-pmgmt/blob/main/app/optimize.py">app/optimize.py</a>

Step 5) Efficient frontier construction and portfolios modelling including:<br/>
-Generate X amout of (1M) of portfolios<br/>
-From those generated portfolios locate the assets weights which:<br/>
    >Minimize the portfolio variance<br/>
    >Maximize the portfolio Sharpe ratio<br/>
-Plot step 4 and 5<br/>

see <a href="https://github.com/Fnine99/markowitz_eff_frontier-pmgmt/blob/main/app/frontier.py">app/frontier.py</a>

# Results Example

Step 2:

Monthly Prices:
<br/>
<img width="400" alt="" src="https://user-images.githubusercontent.com/97029819/229621780-afae2449-1056-44fa-b882-812eec861714.png">

Monthly returns:
<br/>
<img width="400" alt="" src="https://user-images.githubusercontent.com/97029819/229622439-de3e3598-c1a0-4b00-853d-c3625f53f7a0.png">
<br/>

<img width="249" alt="" src="https://user-images.githubusercontent.com/97029819/229622635-98b35520-6c89-41a5-906d-d52ffc1b127f.png">

<img width="249" alt="" src="https://user-images.githubusercontent.com/97029819/229622656-02133da5-e931-42be-a508-741fc610e582.png">

<img width="249" alt="" src="https://user-images.githubusercontent.com/97029819/229622670-c18106c8-f783-4385-bdc1-4b4c3945a855.png">
<br/>


Step 3:
<br/>
<img width="280" alt="" src="https://user-images.githubusercontent.com/97029819/229622676-4c516d11-8c44-407d-920d-924df9237305.png">
<br/>
<br/>
<img width="280" alt="" src="https://user-images.githubusercontent.com/97029819/229622694-dd40d579-43c8-40dc-8749-dd5f033d2829.png">
<br/>


Portfolio Covariance Matrix:
<br/>
<img width="578" alt="" src="https://user-images.githubusercontent.com/97029819/229625478-6b081044-4472-4ae9-b5e1-0f2e26da4c34.png">
<br/>
Portfolio Correlation Matrix:
<br/>
<img width="578" alt="" src="https://user-images.githubusercontent.com/97029819/229625495-2bb7309f-1350-4e3e-b458-6284749e7f6a.png">
<br/>
Portfolio Inverse Covariance Matrix:
<br/>
<img width="726" alt="" src="https://user-images.githubusercontent.com/97029819/229625499-3723f2f2-925f-4238-8979-f8423d9bf746.png">
<br/>
Step 4:<br/>
Note that the portfolio with asset weight bounds of [0.000, 0.900] and with a risk-free rate of 0.045. Very interesting to see that, when generating 1M of portfolios, we can very precisely predict the optimized portfolios. 
<br/>
<img width="292" alt="Screenshot 2023-04-03 at 5 20 00 PM" src="https://user-images.githubusercontent.com/97029819/229630459-615eb57e-60a2-41ef-bc0b-6fd239815815.png">
<br/>
<img width="309" alt="Screenshot 2023-04-03 at 5 20 16 PM" src="https://user-images.githubusercontent.com/97029819/229630460-40ba2ae7-7900-448f-b904-d587ad5ec333.png">
<br/>
<br/>
<img width="571" alt="Screenshot 2023-04-03 at 5 20 38 PM" src="https://user-images.githubusercontent.com/97029819/229630462-c3822a7e-37db-419d-b414-d6a7423ae72a.png">
<br/>
<br/>
<img width="571" alt="Screenshot 2023-04-03 at 5 20 48 PM" src="https://user-images.githubusercontent.com/97029819/229630463-e028f5dc-fb82-4eda-ba81-86d95c261c0a.png">
<br/>
Step 5:
<br/>
<img width="726" alt="" src="https://user-images.githubusercontent.com/97029819/229627650-f469d53e-420a-4c94-b7b6-046653bdec17.png">
<br/>
<br/>
<img width="726" alt="" src="https://user-images.githubusercontent.com/97029819/229627652-96aff356-f959-4a01-beac-c0fdf1739a2a.png">
<br/>
<br/>
<img width="726" alt="" src="https://user-images.githubusercontent.com/97029819/229627653-e94906eb-9bda-4ecc-8495-cd78c836864d.png">
<br/>
<br/>
<img width="726" alt="" src="https://user-images.githubusercontent.com/97029819/229627654-0273c900-914c-4a21-a7d5-394a1eba88c3.png">
<br/>





