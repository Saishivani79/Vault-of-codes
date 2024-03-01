{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP3s/6FGw7CnJ7bcJQ+NZrj",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Saishivani79/Vaultofcodes/blob/main/saishivani.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 10,
      "metadata": {
        "id": "_8Vo5BGIebNt"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "import plotly.express as px\n",
        "import plotly.graph_objects as go\n",
        "import plotly.io as pio\n",
        "import plotly.colors as colors\n",
        "pio.templates.default=\"plotly_white\"\n",
        "df=pd.read_excel(\"/content/Sample - Superstore.xlsx\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "McAAFy_NgiDc",
        "outputId": "b584116f-279c-4675-9bbd-3fb73fe9b864"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "      Row ID        Order ID Order Date  Ship Date       Ship Mode  \\\n",
              "0          1  CA-2016-152156 2016-11-08 2016-11-11    Second Class   \n",
              "1          2  CA-2016-152156 2016-11-08 2016-11-11    Second Class   \n",
              "2          3  CA-2016-138688 2016-06-12 2016-06-16    Second Class   \n",
              "3          4  US-2015-108966 2015-10-11 2015-10-18  Standard Class   \n",
              "4          5  US-2015-108966 2015-10-11 2015-10-18  Standard Class   \n",
              "...      ...             ...        ...        ...             ...   \n",
              "9989    9990  CA-2014-110422 2014-01-21 2014-01-23    Second Class   \n",
              "9990    9991  CA-2017-121258 2017-02-26 2017-03-03  Standard Class   \n",
              "9991    9992  CA-2017-121258 2017-02-26 2017-03-03  Standard Class   \n",
              "9992    9993  CA-2017-121258 2017-02-26 2017-03-03  Standard Class   \n",
              "9993    9994  CA-2017-119914 2017-05-04 2017-05-09    Second Class   \n",
              "\n",
              "     Customer ID     Customer Name    Segment        Country             City  \\\n",
              "0       CG-12520       Claire Gute   Consumer  United States        Henderson   \n",
              "1       CG-12520       Claire Gute   Consumer  United States        Henderson   \n",
              "2       DV-13045   Darrin Van Huff  Corporate  United States      Los Angeles   \n",
              "3       SO-20335    Sean O'Donnell   Consumer  United States  Fort Lauderdale   \n",
              "4       SO-20335    Sean O'Donnell   Consumer  United States  Fort Lauderdale   \n",
              "...          ...               ...        ...            ...              ...   \n",
              "9989    TB-21400  Tom Boeckenhauer   Consumer  United States            Miami   \n",
              "9990    DB-13060       Dave Brooks   Consumer  United States       Costa Mesa   \n",
              "9991    DB-13060       Dave Brooks   Consumer  United States       Costa Mesa   \n",
              "9992    DB-13060       Dave Brooks   Consumer  United States       Costa Mesa   \n",
              "9993    CC-12220      Chris Cortes   Consumer  United States      Westminster   \n",
              "\n",
              "      ... Postal Code  Region       Product ID         Category Sub-Category  \\\n",
              "0     ...       42420   South  FUR-BO-10001798        Furniture    Bookcases   \n",
              "1     ...       42420   South  FUR-CH-10000454        Furniture       Chairs   \n",
              "2     ...       90036    West  OFF-LA-10000240  Office Supplies       Labels   \n",
              "3     ...       33311   South  FUR-TA-10000577        Furniture       Tables   \n",
              "4     ...       33311   South  OFF-ST-10000760  Office Supplies      Storage   \n",
              "...   ...         ...     ...              ...              ...          ...   \n",
              "9989  ...       33180   South  FUR-FU-10001889        Furniture  Furnishings   \n",
              "9990  ...       92627    West  FUR-FU-10000747        Furniture  Furnishings   \n",
              "9991  ...       92627    West  TEC-PH-10003645       Technology       Phones   \n",
              "9992  ...       92627    West  OFF-PA-10004041  Office Supplies        Paper   \n",
              "9993  ...       92683    West  OFF-AP-10002684  Office Supplies   Appliances   \n",
              "\n",
              "                                           Product Name     Sales  Quantity  \\\n",
              "0                     Bush Somerset Collection Bookcase  261.9600         2   \n",
              "1     Hon Deluxe Fabric Upholstered Stacking Chairs,...  731.9400         3   \n",
              "2     Self-Adhesive Address Labels for Typewriters b...   14.6200         2   \n",
              "3         Bretford CR4500 Series Slim Rectangular Table  957.5775         5   \n",
              "4                        Eldon Fold 'N Roll Cart System   22.3680         2   \n",
              "...                                                 ...       ...       ...   \n",
              "9989                             Ultra Door Pull Handle   25.2480         3   \n",
              "9990  Tenex B1-RE Series Chair Mats for Low Pile Car...   91.9600         2   \n",
              "9991                              Aastra 57i VoIP phone  258.5760         2   \n",
              "9992  It's Hot Message Books with Stickers, 2 3/4\" x 5\"   29.6000         4   \n",
              "9993  Acco 7-Outlet Masterpiece Power Center, Wihtou...  243.1600         2   \n",
              "\n",
              "      Discount    Profit  \n",
              "0         0.00   41.9136  \n",
              "1         0.00  219.5820  \n",
              "2         0.00    6.8714  \n",
              "3         0.45 -383.0310  \n",
              "4         0.20    2.5164  \n",
              "...        ...       ...  \n",
              "9989      0.20    4.1028  \n",
              "9990      0.00   15.6332  \n",
              "9991      0.20   19.3932  \n",
              "9992      0.00   13.3200  \n",
              "9993      0.00   72.9480  \n",
              "\n",
              "[9994 rows x 21 columns]"
            ],
            "text/html": [
              "\n",
              "  <div id=\"df-b84b0b5d-2940-487e-a0b9-b20cebd0ff7b\" class=\"colab-df-container\">\n",
              "    <div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Row ID</th>\n",
              "      <th>Order ID</th>\n",
              "      <th>Order Date</th>\n",
              "      <th>Ship Date</th>\n",
              "      <th>Ship Mode</th>\n",
              "      <th>Customer ID</th>\n",
              "      <th>Customer Name</th>\n",
              "      <th>Segment</th>\n",
              "      <th>Country</th>\n",
              "      <th>City</th>\n",
              "      <th>...</th>\n",
              "      <th>Postal Code</th>\n",
              "      <th>Region</th>\n",
              "      <th>Product ID</th>\n",
              "      <th>Category</th>\n",
              "      <th>Sub-Category</th>\n",
              "      <th>Product Name</th>\n",
              "      <th>Sales</th>\n",
              "      <th>Quantity</th>\n",
              "      <th>Discount</th>\n",
              "      <th>Profit</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>1</td>\n",
              "      <td>CA-2016-152156</td>\n",
              "      <td>2016-11-08</td>\n",
              "      <td>2016-11-11</td>\n",
              "      <td>Second Class</td>\n",
              "      <td>CG-12520</td>\n",
              "      <td>Claire Gute</td>\n",
              "      <td>Consumer</td>\n",
              "      <td>United States</td>\n",
              "      <td>Henderson</td>\n",
              "      <td>...</td>\n",
              "      <td>42420</td>\n",
              "      <td>South</td>\n",
              "      <td>FUR-BO-10001798</td>\n",
              "      <td>Furniture</td>\n",
              "      <td>Bookcases</td>\n",
              "      <td>Bush Somerset Collection Bookcase</td>\n",
              "      <td>261.9600</td>\n",
              "      <td>2</td>\n",
              "      <td>0.00</td>\n",
              "      <td>41.9136</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2</td>\n",
              "      <td>CA-2016-152156</td>\n",
              "      <td>2016-11-08</td>\n",
              "      <td>2016-11-11</td>\n",
              "      <td>Second Class</td>\n",
              "      <td>CG-12520</td>\n",
              "      <td>Claire Gute</td>\n",
              "      <td>Consumer</td>\n",
              "      <td>United States</td>\n",
              "      <td>Henderson</td>\n",
              "      <td>...</td>\n",
              "      <td>42420</td>\n",
              "      <td>South</td>\n",
              "      <td>FUR-CH-10000454</td>\n",
              "      <td>Furniture</td>\n",
              "      <td>Chairs</td>\n",
              "      <td>Hon Deluxe Fabric Upholstered Stacking Chairs,...</td>\n",
              "      <td>731.9400</td>\n",
              "      <td>3</td>\n",
              "      <td>0.00</td>\n",
              "      <td>219.5820</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>3</td>\n",
              "      <td>CA-2016-138688</td>\n",
              "      <td>2016-06-12</td>\n",
              "      <td>2016-06-16</td>\n",
              "      <td>Second Class</td>\n",
              "      <td>DV-13045</td>\n",
              "      <td>Darrin Van Huff</td>\n",
              "      <td>Corporate</td>\n",
              "      <td>United States</td>\n",
              "      <td>Los Angeles</td>\n",
              "      <td>...</td>\n",
              "      <td>90036</td>\n",
              "      <td>West</td>\n",
              "      <td>OFF-LA-10000240</td>\n",
              "      <td>Office Supplies</td>\n",
              "      <td>Labels</td>\n",
              "      <td>Self-Adhesive Address Labels for Typewriters b...</td>\n",
              "      <td>14.6200</td>\n",
              "      <td>2</td>\n",
              "      <td>0.00</td>\n",
              "      <td>6.8714</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>4</td>\n",
              "      <td>US-2015-108966</td>\n",
              "      <td>2015-10-11</td>\n",
              "      <td>2015-10-18</td>\n",
              "      <td>Standard Class</td>\n",
              "      <td>SO-20335</td>\n",
              "      <td>Sean O'Donnell</td>\n",
              "      <td>Consumer</td>\n",
              "      <td>United States</td>\n",
              "      <td>Fort Lauderdale</td>\n",
              "      <td>...</td>\n",
              "      <td>33311</td>\n",
              "      <td>South</td>\n",
              "      <td>FUR-TA-10000577</td>\n",
              "      <td>Furniture</td>\n",
              "      <td>Tables</td>\n",
              "      <td>Bretford CR4500 Series Slim Rectangular Table</td>\n",
              "      <td>957.5775</td>\n",
              "      <td>5</td>\n",
              "      <td>0.45</td>\n",
              "      <td>-383.0310</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>5</td>\n",
              "      <td>US-2015-108966</td>\n",
              "      <td>2015-10-11</td>\n",
              "      <td>2015-10-18</td>\n",
              "      <td>Standard Class</td>\n",
              "      <td>SO-20335</td>\n",
              "      <td>Sean O'Donnell</td>\n",
              "      <td>Consumer</td>\n",
              "      <td>United States</td>\n",
              "      <td>Fort Lauderdale</td>\n",
              "      <td>...</td>\n",
              "      <td>33311</td>\n",
              "      <td>South</td>\n",
              "      <td>OFF-ST-10000760</td>\n",
              "      <td>Office Supplies</td>\n",
              "      <td>Storage</td>\n",
              "      <td>Eldon Fold 'N Roll Cart System</td>\n",
              "      <td>22.3680</td>\n",
              "      <td>2</td>\n",
              "      <td>0.20</td>\n",
              "      <td>2.5164</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>...</th>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "      <td>...</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9989</th>\n",
              "      <td>9990</td>\n",
              "      <td>CA-2014-110422</td>\n",
              "      <td>2014-01-21</td>\n",
              "      <td>2014-01-23</td>\n",
              "      <td>Second Class</td>\n",
              "      <td>TB-21400</td>\n",
              "      <td>Tom Boeckenhauer</td>\n",
              "      <td>Consumer</td>\n",
              "      <td>United States</td>\n",
              "      <td>Miami</td>\n",
              "      <td>...</td>\n",
              "      <td>33180</td>\n",
              "      <td>South</td>\n",
              "      <td>FUR-FU-10001889</td>\n",
              "      <td>Furniture</td>\n",
              "      <td>Furnishings</td>\n",
              "      <td>Ultra Door Pull Handle</td>\n",
              "      <td>25.2480</td>\n",
              "      <td>3</td>\n",
              "      <td>0.20</td>\n",
              "      <td>4.1028</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9990</th>\n",
              "      <td>9991</td>\n",
              "      <td>CA-2017-121258</td>\n",
              "      <td>2017-02-26</td>\n",
              "      <td>2017-03-03</td>\n",
              "      <td>Standard Class</td>\n",
              "      <td>DB-13060</td>\n",
              "      <td>Dave Brooks</td>\n",
              "      <td>Consumer</td>\n",
              "      <td>United States</td>\n",
              "      <td>Costa Mesa</td>\n",
              "      <td>...</td>\n",
              "      <td>92627</td>\n",
              "      <td>West</td>\n",
              "      <td>FUR-FU-10000747</td>\n",
              "      <td>Furniture</td>\n",
              "      <td>Furnishings</td>\n",
              "      <td>Tenex B1-RE Series Chair Mats for Low Pile Car...</td>\n",
              "      <td>91.9600</td>\n",
              "      <td>2</td>\n",
              "      <td>0.00</td>\n",
              "      <td>15.6332</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9991</th>\n",
              "      <td>9992</td>\n",
              "      <td>CA-2017-121258</td>\n",
              "      <td>2017-02-26</td>\n",
              "      <td>2017-03-03</td>\n",
              "      <td>Standard Class</td>\n",
              "      <td>DB-13060</td>\n",
              "      <td>Dave Brooks</td>\n",
              "      <td>Consumer</td>\n",
              "      <td>United States</td>\n",
              "      <td>Costa Mesa</td>\n",
              "      <td>...</td>\n",
              "      <td>92627</td>\n",
              "      <td>West</td>\n",
              "      <td>TEC-PH-10003645</td>\n",
              "      <td>Technology</td>\n",
              "      <td>Phones</td>\n",
              "      <td>Aastra 57i VoIP phone</td>\n",
              "      <td>258.5760</td>\n",
              "      <td>2</td>\n",
              "      <td>0.20</td>\n",
              "      <td>19.3932</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9992</th>\n",
              "      <td>9993</td>\n",
              "      <td>CA-2017-121258</td>\n",
              "      <td>2017-02-26</td>\n",
              "      <td>2017-03-03</td>\n",
              "      <td>Standard Class</td>\n",
              "      <td>DB-13060</td>\n",
              "      <td>Dave Brooks</td>\n",
              "      <td>Consumer</td>\n",
              "      <td>United States</td>\n",
              "      <td>Costa Mesa</td>\n",
              "      <td>...</td>\n",
              "      <td>92627</td>\n",
              "      <td>West</td>\n",
              "      <td>OFF-PA-10004041</td>\n",
              "      <td>Office Supplies</td>\n",
              "      <td>Paper</td>\n",
              "      <td>It's Hot Message Books with Stickers, 2 3/4\" x 5\"</td>\n",
              "      <td>29.6000</td>\n",
              "      <td>4</td>\n",
              "      <td>0.00</td>\n",
              "      <td>13.3200</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>9993</th>\n",
              "      <td>9994</td>\n",
              "      <td>CA-2017-119914</td>\n",
              "      <td>2017-05-04</td>\n",
              "      <td>2017-05-09</td>\n",
              "      <td>Second Class</td>\n",
              "      <td>CC-12220</td>\n",
              "      <td>Chris Cortes</td>\n",
              "      <td>Consumer</td>\n",
              "      <td>United States</td>\n",
              "      <td>Westminster</td>\n",
              "      <td>...</td>\n",
              "      <td>92683</td>\n",
              "      <td>West</td>\n",
              "      <td>OFF-AP-10002684</td>\n",
              "      <td>Office Supplies</td>\n",
              "      <td>Appliances</td>\n",
              "      <td>Acco 7-Outlet Masterpiece Power Center, Wihtou...</td>\n",
              "      <td>243.1600</td>\n",
              "      <td>2</td>\n",
              "      <td>0.00</td>\n",
              "      <td>72.9480</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "<p>9994 rows × 21 columns</p>\n",
              "</div>\n",
              "    <div class=\"colab-df-buttons\">\n",
              "\n",
              "  <div class=\"colab-df-container\">\n",
              "    <button class=\"colab-df-convert\" onclick=\"convertToInteractive('df-b84b0b5d-2940-487e-a0b9-b20cebd0ff7b')\"\n",
              "            title=\"Convert this dataframe to an interactive table.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\" viewBox=\"0 -960 960 960\">\n",
              "    <path d=\"M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "\n",
              "  <style>\n",
              "    .colab-df-container {\n",
              "      display:flex;\n",
              "      gap: 12px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert {\n",
              "      background-color: #E8F0FE;\n",
              "      border: none;\n",
              "      border-radius: 50%;\n",
              "      cursor: pointer;\n",
              "      display: none;\n",
              "      fill: #1967D2;\n",
              "      height: 32px;\n",
              "      padding: 0 0 0 0;\n",
              "      width: 32px;\n",
              "    }\n",
              "\n",
              "    .colab-df-convert:hover {\n",
              "      background-color: #E2EBFA;\n",
              "      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "      fill: #174EA6;\n",
              "    }\n",
              "\n",
              "    .colab-df-buttons div {\n",
              "      margin-bottom: 4px;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert {\n",
              "      background-color: #3B4455;\n",
              "      fill: #D2E3FC;\n",
              "    }\n",
              "\n",
              "    [theme=dark] .colab-df-convert:hover {\n",
              "      background-color: #434B5C;\n",
              "      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "      fill: #FFFFFF;\n",
              "    }\n",
              "  </style>\n",
              "\n",
              "    <script>\n",
              "      const buttonEl =\n",
              "        document.querySelector('#df-b84b0b5d-2940-487e-a0b9-b20cebd0ff7b button.colab-df-convert');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      async function convertToInteractive(key) {\n",
              "        const element = document.querySelector('#df-b84b0b5d-2940-487e-a0b9-b20cebd0ff7b');\n",
              "        const dataTable =\n",
              "          await google.colab.kernel.invokeFunction('convertToInteractive',\n",
              "                                                    [key], {});\n",
              "        if (!dataTable) return;\n",
              "\n",
              "        const docLinkHtml = 'Like what you see? Visit the ' +\n",
              "          '<a target=\"_blank\" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'\n",
              "          + ' to learn more about interactive tables.';\n",
              "        element.innerHTML = '';\n",
              "        dataTable['output_type'] = 'display_data';\n",
              "        await google.colab.output.renderOutput(dataTable, element);\n",
              "        const docLink = document.createElement('div');\n",
              "        docLink.innerHTML = docLinkHtml;\n",
              "        element.appendChild(docLink);\n",
              "      }\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "\n",
              "<div id=\"df-466141f8-9d42-422f-a228-a2f8a543a400\">\n",
              "  <button class=\"colab-df-quickchart\" onclick=\"quickchart('df-466141f8-9d42-422f-a228-a2f8a543a400')\"\n",
              "            title=\"Suggest charts\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "<svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "     width=\"24px\">\n",
              "    <g>\n",
              "        <path d=\"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z\"/>\n",
              "    </g>\n",
              "</svg>\n",
              "  </button>\n",
              "\n",
              "<style>\n",
              "  .colab-df-quickchart {\n",
              "      --bg-color: #E8F0FE;\n",
              "      --fill-color: #1967D2;\n",
              "      --hover-bg-color: #E2EBFA;\n",
              "      --hover-fill-color: #174EA6;\n",
              "      --disabled-fill-color: #AAA;\n",
              "      --disabled-bg-color: #DDD;\n",
              "  }\n",
              "\n",
              "  [theme=dark] .colab-df-quickchart {\n",
              "      --bg-color: #3B4455;\n",
              "      --fill-color: #D2E3FC;\n",
              "      --hover-bg-color: #434B5C;\n",
              "      --hover-fill-color: #FFFFFF;\n",
              "      --disabled-bg-color: #3B4455;\n",
              "      --disabled-fill-color: #666;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart {\n",
              "    background-color: var(--bg-color);\n",
              "    border: none;\n",
              "    border-radius: 50%;\n",
              "    cursor: pointer;\n",
              "    display: none;\n",
              "    fill: var(--fill-color);\n",
              "    height: 32px;\n",
              "    padding: 0;\n",
              "    width: 32px;\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart:hover {\n",
              "    background-color: var(--hover-bg-color);\n",
              "    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "    fill: var(--button-hover-fill-color);\n",
              "  }\n",
              "\n",
              "  .colab-df-quickchart-complete:disabled,\n",
              "  .colab-df-quickchart-complete:disabled:hover {\n",
              "    background-color: var(--disabled-bg-color);\n",
              "    fill: var(--disabled-fill-color);\n",
              "    box-shadow: none;\n",
              "  }\n",
              "\n",
              "  .colab-df-spinner {\n",
              "    border: 2px solid var(--fill-color);\n",
              "    border-color: transparent;\n",
              "    border-bottom-color: var(--fill-color);\n",
              "    animation:\n",
              "      spin 1s steps(1) infinite;\n",
              "  }\n",
              "\n",
              "  @keyframes spin {\n",
              "    0% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "      border-left-color: var(--fill-color);\n",
              "    }\n",
              "    20% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    30% {\n",
              "      border-color: transparent;\n",
              "      border-left-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    40% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-top-color: var(--fill-color);\n",
              "    }\n",
              "    60% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "    }\n",
              "    80% {\n",
              "      border-color: transparent;\n",
              "      border-right-color: var(--fill-color);\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "    90% {\n",
              "      border-color: transparent;\n",
              "      border-bottom-color: var(--fill-color);\n",
              "    }\n",
              "  }\n",
              "</style>\n",
              "\n",
              "  <script>\n",
              "    async function quickchart(key) {\n",
              "      const quickchartButtonEl =\n",
              "        document.querySelector('#' + key + ' button');\n",
              "      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.\n",
              "      quickchartButtonEl.classList.add('colab-df-spinner');\n",
              "      try {\n",
              "        const charts = await google.colab.kernel.invokeFunction(\n",
              "            'suggestCharts', [key], {});\n",
              "      } catch (error) {\n",
              "        console.error('Error during call to suggestCharts:', error);\n",
              "      }\n",
              "      quickchartButtonEl.classList.remove('colab-df-spinner');\n",
              "      quickchartButtonEl.classList.add('colab-df-quickchart-complete');\n",
              "    }\n",
              "    (() => {\n",
              "      let quickchartButtonEl =\n",
              "        document.querySelector('#df-466141f8-9d42-422f-a228-a2f8a543a400 button');\n",
              "      quickchartButtonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "    })();\n",
              "  </script>\n",
              "</div>\n",
              "\n",
              "  <div id=\"id_4c9e0a91-8be2-477d-b8e2-8762fa1040db\">\n",
              "    <style>\n",
              "      .colab-df-generate {\n",
              "        background-color: #E8F0FE;\n",
              "        border: none;\n",
              "        border-radius: 50%;\n",
              "        cursor: pointer;\n",
              "        display: none;\n",
              "        fill: #1967D2;\n",
              "        height: 32px;\n",
              "        padding: 0 0 0 0;\n",
              "        width: 32px;\n",
              "      }\n",
              "\n",
              "      .colab-df-generate:hover {\n",
              "        background-color: #E2EBFA;\n",
              "        box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);\n",
              "        fill: #174EA6;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate {\n",
              "        background-color: #3B4455;\n",
              "        fill: #D2E3FC;\n",
              "      }\n",
              "\n",
              "      [theme=dark] .colab-df-generate:hover {\n",
              "        background-color: #434B5C;\n",
              "        box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);\n",
              "        filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));\n",
              "        fill: #FFFFFF;\n",
              "      }\n",
              "    </style>\n",
              "    <button class=\"colab-df-generate\" onclick=\"generateWithVariable('df')\"\n",
              "            title=\"Generate code using this dataframe.\"\n",
              "            style=\"display:none;\">\n",
              "\n",
              "  <svg xmlns=\"http://www.w3.org/2000/svg\" height=\"24px\"viewBox=\"0 0 24 24\"\n",
              "       width=\"24px\">\n",
              "    <path d=\"M7,19H8.4L18.45,9,17,7.55,7,17.6ZM5,21V16.75L18.45,3.32a2,2,0,0,1,2.83,0l1.4,1.43a1.91,1.91,0,0,1,.58,1.4,1.91,1.91,0,0,1-.58,1.4L9.25,21ZM18.45,9,17,7.55Zm-12,3A5.31,5.31,0,0,0,4.9,8.1,5.31,5.31,0,0,0,1,6.5,5.31,5.31,0,0,0,4.9,4.9,5.31,5.31,0,0,0,6.5,1,5.31,5.31,0,0,0,8.1,4.9,5.31,5.31,0,0,0,12,6.5,5.46,5.46,0,0,0,6.5,12Z\"/>\n",
              "  </svg>\n",
              "    </button>\n",
              "    <script>\n",
              "      (() => {\n",
              "      const buttonEl =\n",
              "        document.querySelector('#id_4c9e0a91-8be2-477d-b8e2-8762fa1040db button.colab-df-generate');\n",
              "      buttonEl.style.display =\n",
              "        google.colab.kernel.accessAllowed ? 'block' : 'none';\n",
              "\n",
              "      buttonEl.onclick = () => {\n",
              "        google.colab.notebook.generateWithVariable('df');\n",
              "      }\n",
              "      })();\n",
              "    </script>\n",
              "  </div>\n",
              "\n",
              "    </div>\n",
              "  </div>\n"
            ],
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "dataframe",
              "variable_name": "df"
            }
          },
          "metadata": {},
          "execution_count": 20
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#salesbycategory\n",
        "sales_by_category=df.groupby(\"Category\")[\"Sales\"].sum().reset_index()\n",
        "print(sales_by_category)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FBGMH1SYjync",
        "outputId": "b56fbc99-a263-4cff-f1c5-7ae90d6e5d5e"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "          Category        Sales\n",
            "0        Furniture  741999.7953\n",
            "1  Office Supplies  719047.0320\n",
            "2       Technology  836154.0330\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#salesbycategory\n",
        "sales_by_category=df.groupby(\"Category\")[\"Sales\"].sum().reset_index().plot(kind=\"area\")\n",
        "print(sales_by_category)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 448
        },
        "id": "Gktbc_eMkmSC",
        "outputId": "60195787-8ea5-4464-a093-df543bd01556"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Axes(0.125,0.11;0.775x0.77)\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAkIAAAGdCAYAAAD+JxxnAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAABCK0lEQVR4nO3de3wU9b3/8Xdum4TLJnJJQg4BYlEhyKUECbHeOEZWDRw5ogVLNeUiRxo4hlS5tBpE7QGxyqUgOVZr6KmUy68VK0gQQoEWIkggCiiINppY2ASFZCFAbju/P2imWQgkCwm5zOv5eOyjZuazM5/vTsK+OzvfWR/DMAwBAABYkG9TNwAAANBUCEIAAMCyCEIAAMCyCEIAAMCyCEIAAMCyCEIAAMCyCEIAAMCyCEIAAMCy/Ju6gebM7Xbr6NGjat++vXx8fJq6HQAAUA+GYejUqVOKjIyUr+/lz/kQhC7j6NGjioqKauo2AADAFSgoKFDXrl0vW0MQuoz27dtLOv9C2u32Ju4GAADUh8vlUlRUlPk+fjkEocuo/jjMbrcThAAAaGHqc1kLF0sDAADLIggBAADLIggBAADL4hqhq2QYhiorK1VVVdXUrbQKfn5+8vf353YFAIBrgiB0FcrLy3Xs2DGdOXOmqVtpVdq0aaMuXbrIZrM1dSsAgFaOIHSF3G638vLy5Ofnp8jISNlsNs5iXCXDMFReXq7jx48rLy9PN9xwQ503wgIA4GoQhK5QeXm53G63oqKi1KZNm6Zup9UIDg5WQECAvv76a5WXlysoKKipWwIAtGL83+2rxBmLhsdrCgC4VnjHAQAAlsVHY43gH8VndbK0/Jrt77q2Nv1baPA12x8AAK0FQaiB/aP4rP79V1tVVum+ZvsM9PfVlqfuuqZhKCMjQykpKSouLr5m+wQAoKHx0VgDO1lafk1DkCSVVbq9PgN1/PhxTZ48Wd26dVNgYKAiIiLkcDi0Y8eORuoSAIDmhzNCFjVq1CiVl5dr+fLluv7661VYWKisrCx99913Td0aAADXDGeELKi4uFh//etf9dJLL2no0KHq3r27Bg8erFmzZuk//uM/JEmvvvqq+vbtq7Zt2yoqKko//elPdfr06ctu991339XAgQMVFBSk66+/XnPmzFFlZaWk8/cIeu6558wzUJGRkfrv//7vRh8rAKB5OVlarr8cLtKrmz7Xo2/u0rRVuU3aD2eELKhdu3Zq166d1q5dqyFDhigwMPCiGl9fXy1evFjR0dH6+9//rp/+9KeaPn26XnvttVq3+de//lWPPfaYFi9erNtvv11ffvmlJk2aJEmaPXu2/vjHP2rBggVauXKl+vTpI6fTqY8//rhRxwkAaFqVVW4dcp7SvoJi7cs/qdz8Yv3921KPGn9fH736w/5NdlNigpAF+fv7KyMjQ48//rjS09M1cOBA3XnnnRozZoz69esnSUpJSTHre/TooRdffFFPPPHEJYPQnDlzNHPmTCUlJUmSrr/+er3wwguaPn26Zs+erfz8fEVERCghIUEBAQHq1q2bBg8e3OhjBQBcO4Wuc9qXX6x9BSe1L79Y+78p0dmK2r+L00eSIanSbVzTHi9EELKoUaNGKTExUX/961/14YcfasOGDZo/f77eeOMN/eQnP9HmzZs1d+5cHTp0SC6XS5WVlTp37pzOnDlT6520P/74Y+3YsUO//OUvzWVVVVXmcx5++GEtXLhQ119/ve69917df//9GjFihPz9+RUEgJboXEWVDh4tOR98/hl+jhafq/fza8afpvyKKt6FLCwoKEj33HOP7rnnHj377LOaOHGiZs+erbvuukvDhw/X5MmT9ctf/lIdOnTQ3/72N02YMEHl5eW1BqHTp09rzpw5evDBB2vdT1RUlA4fPqzNmzdr06ZN+ulPf6qXX35Z27ZtU0BAwLUYLgDgChmGoYITZ80zPfvyT+rgUdclz+ZUn+1pCQhCMMXExGjt2rXKycmR2+3WK6+8Yn7dxerVqy/73IEDB+rw4cPq2bPnJWuCg4M1YsQIjRgxQsnJyerVq5f279+vgQMHNug4AABX53RZpT4pKDav7dmbX6wTXtympaWEIIkgZEnfffedHn74YY0fP179+vVT+/bttWfPHs2fP18PPPCAevbsqYqKCv3617/WiBEjtGPHDqWnp192m2lpaRo+fLi6deumhx56SL6+vvr444914MABvfjii8rIyFBVVZXi4uLUpk0b/f73v1dwcLC6d+9+jUYNAKiN223oy+OnPa7t+bzwlC516U5LOttTHwShBnZdW5sC/X2v+Z2lr2trq3d9u3btFBcXpwULFujLL79URUWFoqKi9Pjjj+vnP/+5goOD9eqrr+qll17SrFmzdMcdd2ju3Ll67LHHLrlNh8OhdevW6fnnn9dLL72kgIAA9erVSxMnTpQkhYaGat68eUpNTVVVVZX69u2r9957Tx07drzq8QMA6u9kably/3mm5/wZn2KdLqustba20NOaQpAk+RiG0drG1GBcLpdCQkJUUlIiu93use7cuXPKy8tTdHS0goKCPNbxXWNX53KvLQCg/iqq3DrsPHU+9OSf/6gr74Lp6zU11dmer+YlNuj2Lvf+fSHOCDWCfwsNblXBBADQMpyfvn7SnMn1yT+Kda6i9k8orHC2pz4IQgAAtEAXTV/PP6mjJVc2fd3KCEIAADRzrXn6elPz6rvGqqqq9Oyzzyo6OlrBwcH63ve+pxdeeEE1LzMyDENpaWnq0qWLgoODlZCQoCNHjnhs58SJExo7dqzsdrtCQ0M1YcKEi77H6pNPPtHtt99u3oNm/vz5F/WzZs0a9erVS0FBQerbt6/ef/99j/X16QUAgObm1LkK7fjiWy3ZckQTl3+k2Bc3646X/6InV+YqY+dX+vibksvekZkQVH9enRF66aWXtGzZMi1fvlx9+vTRnj17NG7cOIWEhJhfoDl//nwtXrxYy5cvV3R0tJ599lk5HA59+umn5oWvY8eO1bFjx7Rp0yZVVFRo3LhxmjRpklasWCHp/EVOw4YNU0JCgtLT07V//36NHz9eoaGh5vdX7dy5U4888ojmzp2r4cOHa8WKFRo5cqT27t2rm2++ud69XC2uNW94vKYArMTtNvTF8dMe1/Z8XnjqkmGGsz0Ny6tZY8OHD1d4eLjefPNNc9moUaMUHBys3//+9zIMQ5GRkfrZz36mp556SpJUUlKi8PBwZWRkaMyYMfrss88UExOjjz76SIMGDZIkZWZm6v7779c333yjyMhILVu2TL/4xS/kdDpls52fFj5z5kytXbtWhw4dkiSNHj1apaWlWrdundnLkCFDNGDAAKWnp9erl7pc7qrzqqoqff755woLC2MKeAP77rvvVFRUpBtvvFF+fn5N3Q4ANKgTpeXKLfhX6Mkt8G76emvUYmaN3XrrrXr99df1+eef68Ybb9THH3+sv/3tb3r11VclSXl5eXI6nUpISDCfExISori4OGVnZ2vMmDHKzs5WaGioGYIkKSEhQb6+vtq1a5f+8z//U9nZ2brjjjvMECSdv0/NSy+9pJMnT+q6665Tdna2UlNTPfpzOBxau3ZtvXu5UFlZmcrKysyfXS7XJV8LPz8/hYaGqqioSJLUpk2bJv2ulNbAMAydOXNGRUVFCg0NJQQBaPEqqtw6dOyUx7U9X3135pL1FwYfK4SgpuZVEJo5c6ZcLpd69eolPz8/VVVV6Ze//KXGjh0rSXI6nZKk8PBwj+eFh4eb65xOp8LCwjyb8PdXhw4dPGqio6Mv2kb1uuuuu05Op7PO/dTVy4Xmzp2rOXPm1OOVOC8iIkKSzDCEhhEaGmq+tgDQkjhLztW4UeFJffJNySVvsMv09ebBqyC0evVqvf3221qxYoX69Omj3NxcpaSkKDIyUklJSY3V4zUza9Ysj7NMLpdLUVFRl6z38fFRly5dFBYWpoqKimvRYqsXEBDAmSAALcK5iiod+EeJx1dTHLvM9HXO9jRPXgWhp59+WjNnzjQ/Vurbt6++/vprzZ07V0lJSeb/iy8sLFSXLl3M5xUWFmrAgAGSzp9FufAMSmVlpU6cOGE+PyIiQoWFhR411T/XVVNzfV29XCgwMFCBgYH1ezFq8PPz480bAFoxwzCUf+KM+fHWvoJiferl9HWCT/Pk1fT5M2fOmN9GXs3Pz09u9/nTftHR0YqIiFBWVpa53uVyadeuXYqPj5ckxcfHq7i4WDk5OWbNli1b5Ha7FRcXZ9Zs377d4yzLpk2bdNNNN+m6664za2rup7qmej/16QUAgNrUnL4+IeMjxb6wWXe+vFUpq3K1PPtrfcL09VbDqzNCI0aM0C9/+Ut169ZNffr00b59+/Tqq69q/Pjxks5/VJSSkqIXX3xRN9xwgzllPTIyUiNHjpQk9e7dW/fee68ef/xxpaenq6KiQlOmTNGYMWMUGRkpSfrRj36kOXPmaMKECZoxY4YOHDigRYsWacGCBWYvTz75pO6880698sorSkxM1MqVK7Vnzx69/vrr9e4FAACmr1ubV0Ho17/+tZ599ln99Kc/VVFRkSIjI/Vf//VfSktLM2umT5+u0tJSTZo0ScXFxbrtttuUmZnpcd+et99+W1OmTNHdd98tX19fjRo1SosXLzbXh4SE6IMPPlBycrJiY2PVqVMnpaWlmfcQks7PYFuxYoWeeeYZ/fznP9cNN9ygtWvXmvcQqm8vAABrudrp64Sg1oVvn78Mb+5DAABofq52+jqujRZzHyEAAJqzYyVn/3VBc36x9v+D6eu4PIIQAKBFOldRpf3/KPG4tsfpYvo6vEMQAgA0e4Zh6OvvztT4iKtYnx1j+jquHkEIANDsuM5V6JOCEo+7NJ88U/8b1xJ6UF8EIQBAk6pyG/qiqMb09YKTOlJ4munruCYIQgCAa+q702XKLSg2Q09uQbFKy6pqreUjLjQ2ghAAoNGUV7p1yOnymMn19Qm+fR3NB0EIANBgmL6OloYgBAC4ImfLq3TgKNPX0bIRhAAAdTIMQ199d8YMPbkFTF9H60AQAgBcxHWuQh9XX9Ccf/6CZqavozUiCAGAxVW5DR0pOuVxbc8XRUxfhzUQhADAYr49Xabcf05d35dfrI8LilVazvR1WBNBCABasfJKtz475qpxh+Zi5TN9HTARhACglTAMQ8dKzv3rI66C89PXy5m+DlwSQQgAWqiz5Rd8+3rBSRW6yi5Zz9ke4GIEoSZQUeVWwYkzamPzV7DNT21sfgrw823qtgA0YxdOX99XcFKfHT2lKoPp68DVIAg1gWPF5/Tvr2zzWObv66Ngm5+CAvzU1uanNjZ/tbH5mUHJDE0Bfv9cfuF6PwUH+P/rv2tsI9DfVz4+Pk00WgBX4sLp6/vyi1V8lunrQEMjCDWB8qoqBQf46WzFv2ZpVLoNnTpXqVPnKnW8gffn6yMF+v8rMLUJ9L9MePpn6ArwDFTBAReEruqgFeAnX19CFnA1mL4ONB2CUBPoGdZev37k+5r4uz1XvI2a0aOufxDdhnS2okpnK6r0XekV7/KSbP6+ZnBqa/NXm0A/8+eaH/+dP6NVy5ms6rNbtTyHjwzRGl04fT23oFhnmL4ONAmCUAvV2P8QehO0yivdKq90q8SL0/b1Vf2RYXCAn9rWPJP1z7NRwWbA4iNDNE/llW59Wj19/Z9nfApOnr1kPRc0A9cWQQi1asx/fL0JWTU/MtSpS8+GuRIN8ZGhx/qAGme/+MjQkgzD0NGScx6h58BRF9PXgWaMIIRrrrmELD4yxNU6U16p/d+U/PNGhefDT9FlAjtne4DmhyCEVoWPDP1rfEx4caDiI8MrZxiG8r4tNaeu78sv1qFjTF8HWjqCEOCF5nI2i48MG1/J2RrT1wtOKpfp60CrRBACmonmErIa+yPDQH9fMxi1/efHfU39kWGV29Dnhac8vprii6LTl6xn+jrQehCEAAtoTh8ZllW6VVbpVvGZpv/IsLzSrY8LivXxN0xfB6yKIATgqjWXs1kN8ZEhFzQD1kIQAtCsNXbI4mwPYG3MwQVgWYQeAAQhAABgWV4FoR49esjHx+eiR3JysiTp3LlzSk5OVseOHdWuXTuNGjVKhYWFHtvIz89XYmKi2rRpo7CwMD399NOqrKz0qNm6dasGDhyowMBA9ezZUxkZGRf1snTpUvXo0UNBQUGKi4vT7t27PdbXpxcAAGBtXgWhjz76SMeOHTMfmzZtkiQ9/PDDkqRp06bpvffe05o1a7Rt2zYdPXpUDz74oPn8qqoqJSYmqry8XDt37tTy5cuVkZGhtLQ0syYvL0+JiYkaOnSocnNzlZKSookTJ2rjxo1mzapVq5SamqrZs2dr79696t+/vxwOh4qKisyaunoBAADwMYxL3Ba1HlJSUrRu3TodOXJELpdLnTt31ooVK/TQQw9Jkg4dOqTevXsrOztbQ4YM0YYNGzR8+HAdPXpU4eHhkqT09HTNmDFDx48fl81m04wZM7R+/XodOHDA3M+YMWNUXFyszMxMSVJcXJxuueUWLVmyRJLkdrsVFRWlqVOnaubMmSopKamzl/pwuVwKCQlRSUmJ7Hb7lb5Mtdr8aeFVffs8AACtxVfzEht0e968f1/xNULl5eX6/e9/r/Hjx8vHx0c5OTmqqKhQQkKCWdOrVy9169ZN2dnZkqTs7Gz17dvXDEGS5HA45HK5dPDgQbOm5jaqa6q3UV5erpycHI8aX19fJSQkmDX16QUAAOCKp8+vXbtWxcXF+slPfiJJcjqdstlsCg0N9agLDw+X0+k0a2qGoOr11esuV+NyuXT27FmdPHlSVVVVtdYcOnSo3r3UpqysTGVl/7r3iMvluswrAAAAWrorPiP05ptv6r777lNkZGRD9tOk5s6dq5CQEPMRFRXV1C0BAIBGdEVB6Ouvv9bmzZs1ceJEc1lERITKy8tVXFzsUVtYWKiIiAiz5sKZW9U/11Vjt9sVHBysTp06yc/Pr9aamtuoq5fazJo1SyUlJeajoKCgjlcCAAC0ZFcUhN566y2FhYUpMfFfFzfFxsYqICBAWVlZ5rLDhw8rPz9f8fHxkqT4+Hjt37/fY3bXpk2bZLfbFRMTY9bU3EZ1TfU2bDabYmNjPWrcbreysrLMmvr0UpvAwEDZ7XaPBwAAaL28vkbI7XbrrbfeUlJSkvz9//X0kJAQTZgwQampqerQoYPsdrumTp2q+Ph4c5bWsGHDFBMTo0cffVTz58+X0+nUM888o+TkZAUGBkqSnnjiCS1ZskTTp0/X+PHjtWXLFq1evVrr168395WamqqkpCQNGjRIgwcP1sKFC1VaWqpx48bVuxcAAACvg9DmzZuVn5+v8ePHX7RuwYIF8vX11ahRo1RWViaHw6HXXnvNXO/n56d169Zp8uTJio+PV9u2bZWUlKTnn3/erImOjtb69es1bdo0LVq0SF27dtUbb7whh8Nh1owePVrHjx9XWlqanE6nBgwYoMzMTI8LqOvqBQAA4KruI9TacR8hAAAaX4u8jxAAAEBLRxACAACWRRACAACWRRACAACWRRACAACWRRACAACWRRACAACWRRACAACWRRACAACWRRACAACWRRACAACWRRACAACWRRACAACWRRACAACWRRACAACWRRACAACWRRACAACWRRACAACWRRACAACWRRACAACWRRACAACWRRACAACWRRACAACWRRACAACWRRACAACWRRACAACWRRACAACWRRACAACWRRACAACWRRACAACWRRACAACWRRACAACW5XUQ+sc//qEf//jH6tixo4KDg9W3b1/t2bPHXG8YhtLS0tSlSxcFBwcrISFBR44c8djGiRMnNHbsWNntdoWGhmrChAk6ffq0R80nn3yi22+/XUFBQYqKitL8+fMv6mXNmjXq1auXgoKC1LdvX73//vse6+vTCwAAsC6vgtDJkyf1gx/8QAEBAdqwYYM+/fRTvfLKK7ruuuvMmvnz52vx4sVKT0/Xrl271LZtWzkcDp07d86sGTt2rA4ePKhNmzZp3bp12r59uyZNmmSud7lcGjZsmLp3766cnBy9/PLLeu655/T666+bNTt37tQjjzyiCRMmaN++fRo5cqRGjhypAwcOeNULAACwLh/DMIz6Fs+cOVM7duzQX//611rXG4ahyMhI/exnP9NTTz0lSSopKVF4eLgyMjI0ZswYffbZZ4qJidFHH32kQYMGSZIyMzN1//3365tvvlFkZKSWLVumX/ziF3I6nbLZbOa+165dq0OHDkmSRo8erdLSUq1bt87c/5AhQzRgwAClp6fXq5e6uFwuhYSEqKSkRHa7vb4vU71s/rRQE3+3p+5CAABaua/mJTbo9rx5//bqjNCf//xnDRo0SA8//LDCwsL0/e9/X7/5zW/M9Xl5eXI6nUpI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JMnhcMjlcungwYNmzYXbdjgc5jbKy8uVk5PjUePr66uEhASzpj69XKisrEwul8vjAQAAWi9/b5+wcuVK7d27Vx999NFF65xOp2w2m0JDQz2Wh4eHy+l0mjU1Q1D1+up1l6txuVw6e/asTp48qaqqqlprDh06VO9eLjR37lzNmTPnMqMHAACtiVdnhAoKCvTkk0/q7bffVlBQUGP11GRmzZqlkpIS81FQUNDULQEAgEbkVRDKyclRUVGRBg4cKH9/f/n7+2vbtm1avHix/P39FR4ervLychUXF3s8r7CwUBEREZKkiIiIi2ZuVf9cV43dbldwcLA6deokPz+/WmtqbqOuXi4UGBgou93u8QAAAK2XV0Ho7rvv1v79+5Wbm2s+Bg0apLFjx5r/HRAQoKysLPM5hw8fVn5+vuLj4yVJ8fHx2r9/v8fsrk2bNslutysmJsasqbmN6prqbdhsNsXGxnrUuN1uZWVlmTWxsbF19gIAAKzNq2uE2rdvr5tvvtljWdu2bdWxY0dz+YQJE5SamqoOHTrIbrdr6tSpio+PN2dpDRs2TDExMXr00Uc1f/58OZ1OPfPMM0pOTlZgYKAk6YknntCSJUs0ffp0jR8/Xlu2bNHq1au1fv16c7+pqalKSkrSoEGDNHjwYC1cuFClpaUaN26cJCkkJKTOXgAAgLV5fbF0XRYsWCBfX1+NGjVKZWVlcjgceu2118z1fn5+WrdunSZPnqz4+Hi1bdtWSUlJev75582a6OhorV+/XtOmTdOiRYvUtWtXvfHGG3I4HGbN6NGjdfz4caWlpcnpdGrAgAHKzMz0uIC6rl4AAIC1XdF9hKyC+wgBAND4Wtx9hAAAAFoDghAAALAsghAAALAsghAAALAsghAAALAsghAAALAsghAAALAsghAAALAsghAAALAsghAAALAsghAAALAsghAAALAsghAAALAsghAAALAsghAAALAsghAAALAsghAAALAsghAAALAsghAAALAsghAAALAsghAAALAsghAAALAsghAAALAsghAAALAsghAAALAsghAAALAsghAAALAsghAAALAsghAAALAsghAAALAsghAAALAsr4LQsmXL1K9fP9ntdtntdsXHx2vDhg3m+nPnzik5OVkdO3ZUu3btNGrUKBUWFnpsIz8/X4mJiWrTpo3CwsL09NNPq7Ky0qNm69atGjhwoAIDA9WzZ09lZGRc1MvSpUvVo0cPBQUFKS4uTrt37/ZYX59eAACAtXkVhLp27ap58+YpJydHe/bs0b//+7/rgQce0MGDByVJ06ZN03vvvac1a9Zo27ZtOnr0qB588EHz+VVVVUpMTFR5ebl27typ5cuXKyMjQ2lpaWZNXl6eEhMTNXToUOXm5iolJUUTJ07Uxo0bzZpVq1YpNTVVs2fP1t69e9W/f385HA4VFRWZNXX1AgAA4GMYhnE1G+jQoYNefvllPfTQQ+rcubNWrFihhx56SJJ06NAh9e7dW9nZ2RoyZIg2bNig4cOH6+jRowoPD5ckpaena8aMGTp+/LhsNptmzJih9evX68CBA+Y+xowZo+LiYmVmZkqS4uLidMstt2jJkiWSJLfbraioKE2dOlUzZ85USUlJnb3Uh8vlUkhIiEpKSmS326/mZbrI5k8LNfF3exp0mwAAtERfzUts0O158/59xdcIVVVVaeXKlSotLVV8fLxycnJUUVGhhIQEs6ZXr17q1q2bsrOzJUnZ2dnq27evGYIkyeFwyOVymWeVsrOzPbZRXVO9jfLycuXk5HjU+Pr6KiEhwaypTy+1KSsrk8vl8ngAAIDWy+sgtH//frVr106BgYF64okn9M477ygmJkZOp1M2m02hoaEe9eHh4XI6nZIkp9PpEYKq11evu1yNy+XS2bNn9e2336qqqqrWmprbqKuX2sydO1chISHmIyoqqn4vCgAAaJG8DkI33XSTcnNztWvXLk2ePFlJSUn69NNPG6O3a27WrFkqKSkxHwUFBU3dEgAAaET+3j7BZrOpZ8+ekqTY2Fh99NFHWrRokUaPHq3y8nIVFxd7nIkpLCxURESEJCkiIuKi2V3VM7lq1lw4u6uwsFB2u13BwcHy8/OTn59frTU1t1FXL7UJDAxUYGCgF68GAABoya76PkJut1tlZWWKjY1VQECAsrKyzHWHDx9Wfn6+4uPjJUnx8fHav3+/x+yuTZs2yW63KyYmxqypuY3qmupt2Gw2xcbGetS43W5lZWWZNfXpBQAAwKszQrNmzdJ9992nbt266dSpU1qxYoW2bt2qjRs3KiQkRBMmTFBqaqo6dOggu92uqVOnKj4+3pylNWzYMMXExOjRRx/V/Pnz5XQ69cwzzyg5Odk8E/PEE09oyZIlmj59usaPH68tW7Zo9erVWr9+vdlHamqqkpKSNGjQIA0ePFgLFy5UaWmpxo0bJ0n16gUAAMCrIFRUVKTHHntMx44dU0hIiPr166eNGzfqnnvukSQtWLBAvr6+GjVqlMrKyuRwOPTaa6+Zz/fz89O6des0efJkxcfHq23btkpKStLzzz9v1kRHR2v9+vWaNm2aFi1apK5du+qNN96Qw+Ewa0aPHq3jx48rLS1NTqdTAwYMUGZmpscF1HX1AgAAcNX3EWrNuI8QAACNr0XeRwgAAKClIwgBAADLIggBAADLIggBAADLIggBAADLIggBAADLIggBAADLIggBAADLIggBAADLIggBAADLIggBAADLIggBAADLIggBAADLIggBAADLIggBAADLIggBAADLIggBAADLIggBAADLIggBAADLIggBAADLIggBAADLIggBAADLIggBAADLIggBAADLIggBAADLIggBAADLIggBAADLIggBAADLIggBAADLIggBAADLIggBAADL8ioIzZ07V7fccovat2+vsLAwjRw5UocPH/aoOXfunJKTk9WxY0e1a9dOo0aNUmFhoUdNfn6+EhMT1aZNG4WFhenpp59WZWWlR83WrVs1cOBABQYGqmfPnsrIyLion6VLl6pHjx4KCgpSXFycdu/e7XUvAADAurwKQtu2bVNycrI+/PBDbdq0SRUVFRo2bJhKS0vNmmnTpum9997TmjVrtG3bNh09elQPPvigub6qqkqJiYkqLy/Xzp07tXz5cmVkZCgtLc2sycvLU2JiooYOHarc3FylpKRo4sSJ2rhxo1mzatUqpaamavbs2dq7d6/69+8vh8OhoqKievcCAACszccwDONKn3z8+HGFhYVp27ZtuuOOO1RSUqLOnTtrxYoVeuihhyRJhw4dUu/evZWdna0hQ4Zow4YNGj58uI4eParw8HBJUnp6umbMmKHjx4/LZrNpxowZWr9+vQ4cOGDua8yYMSouLlZmZqYkKS4uTrfccouWLFkiSXK73YqKitLUqVM1c+bMevVSF5fLpZCQEJWUlMhut1/py1SrzZ8WauLv9jToNgEAaIm+mpfYoNvz5v37qq4RKikpkSR16NBBkpSTk6OKigolJCSYNb169VK3bt2UnZ0tScrOzlbfvn3NECRJDodDLpdLBw8eNGtqbqO6pnob5eXlysnJ8ajx9fVVQkKCWVOfXi5UVlYml8vl8QAAAK3XFQcht9utlJQU/eAHP9DNN98sSXI6nbLZbAoNDfWoDQ8Pl9PpNGtqhqDq9dXrLlfjcrl09uxZffvtt6qqqqq1puY26urlQnPnzlVISIj5iIqKquerAQAAWqIrDkLJyck6cOCAVq5c2ZD9NKlZs2appKTEfBQUFDR1SwAAoBH5X8mTpkyZonXr1mn79u3q2rWruTwiIkLl5eUqLi72OBNTWFioiIgIs+bC2V3VM7lq1lw4u6uwsFB2u13BwcHy8/OTn59frTU1t1FXLxcKDAxUYGCgF68EAABoybw6I2QYhqZMmaJ33nlHW7ZsUXR0tMf62NhYBQQEKCsry1x2+PBh5efnKz4+XpIUHx+v/fv3e8zu2rRpk+x2u2JiYsyamtuorqnehs1mU2xsrEeN2+1WVlaWWVOfXgAAgLV5dUYoOTlZK1as0Lvvvqv27dub19qEhIQoODhYISEhmjBhglJTU9WhQwfZ7XZNnTpV8fHx5iytYcOGKSYmRo8++qjmz58vp9OpZ555RsnJyebZmCeeeEJLlizR9OnTNX78eG3ZskWrV6/W+vXrzV5SU1OVlJSkQYMGafDgwVq4cKFKS0s1btw4s6e6egEAANbmVRBatmyZJOmuu+7yWP7WW2/pJz/5iSRpwYIF8vX11ahRo1RWViaHw6HXXnvNrPXz89O6des0efJkxcfHq23btkpKStLzzz9v1kRHR2v9+vWaNm2aFi1apK5du+qNN96Qw+Ewa0aPHq3jx48rLS1NTqdTAwYMUGZmpscF1HX1AgAArO2q7iPU2nEfIQAAGl+LvY8QAABAS0YQAgAAlkUQAgAAlkUQAgAAlkUQAgAAlkUQAgAAlkUQAgAAlkUQAgAAlkUQAgAAlkUQAgAAlkUQAgAAlkUQAgAAlkUQAgAAlkUQAgAAlkUQAgAAlkUQAgAAlkUQAgAAlkUQAgAAlkUQAgAAlkUQAgAAlkUQAgAAlkUQAgAAlkUQAgAAlkUQAgAAlkUQAgAAlkUQAgAAlkUQAgAAlkUQAgAAlkUQAgAAlkUQAgAAlkUQAgAAluV1ENq+fbtGjBihyMhI+fj4aO3atR7rDcNQWlqaunTpouDgYCUkJOjIkSMeNSdOnNDYsWNlt9sVGhqqCRMm6PTp0x41n3zyiW6//XYFBQUpKipK8+fPv6iXNWvWqFevXgoKClLfvn31/vvve90LAACwLq+DUGlpqfr376+lS5fWun7+/PlavHix0tPTtWvXLrVt21YOh0Pnzp0za8aOHauDBw9q06ZNWrdunbZv365JkyaZ610ul4YNG6bu3bsrJydHL7/8sp577jm9/vrrZs3OnTv1yCOPaMKECdq3b59GjhypkSNH6sCBA171AgAArMvHMAzjip/s46N33nlHI0eOlHT+DExkZKR+9rOf6amnnpIklZSUKDw8XBkZGRozZow+++wzxcTE6KOPPtKgQYMkSZmZmbr//vv1zTffKDIyUsuWLdMvfvELOZ1O2Ww2SdLMmTO1du1aHTp0SJI0evRolZaWat26dWY/Q4YM0YABA5Senl6vXuricrkUEhKikpIS2e32K32ZarX500JN/N2eBt0mAAAt0VfzEht0e968fzfoNUJ5eXlyOp1KSEgwl4WEhCguLk7Z2dmSpOzsbIWGhpohSJISEhLk6+urXbt2mTV33HGHGYIkyeFw6PDhwzp58qRZU3M/1TXV+6lPLxcqKyuTy+XyeAAAgNarQYOQ0+mUJIWHh3ssDw8PN9c5nU6FhYV5rPf391eHDh08amrbRs19XKqm5vq6ernQ3LlzFRISYj6ioqLqMWoAANBSMWushlmzZqmkpMR8FBQUNHVLAACgETVoEIqIiJAkFRYWeiwvLCw010VERKioqMhjfWVlpU6cOOFRU9s2au7jUjU119fVy4UCAwNlt9s9HgAAoPVq0CAUHR2tiIgIZWVlmctcLpd27dql+Ph4SVJ8fLyKi4uVk5Nj1mzZskVut1txcXFmzfbt21VRUWHWbNq0STfddJOuu+46s6bmfqprqvdTn14AAIC1eR2ETp8+rdzcXOXm5ko6f1Fybm6u8vPz5ePjo5SUFL344ov685//rP379+uxxx5TZGSkObOsd+/euvfee/X4449r9+7d2rFjh6ZMmaIxY8YoMjJSkvSjH/1INptNEyZM0MGDB7Vq1SotWrRIqampZh9PPvmkMjMz9corr+jQoUN67rnntGfPHk2ZMkWS6tULAACwNn9vn7Bnzx4NHTrU/Lk6nCQlJSkjI0PTp09XaWmpJk2apOLiYt12223KzMxUUFCQ+Zy3335bU6ZM0d133y1fX1+NGjVKixcvNteHhITogw8+UHJysmJjY9WpUyelpaV53Gvo1ltv1YoVK/TMM8/o5z//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qYv+Bo8cOaLIyEhdf/31Gjt2rPLz85uowyszYMAAdenSRffcc4927NhhLm9tx086/zeYkJCg7t27eyxvjsewpKREki76faupubwXEoSu0rfffquqqqqL7lQdHh5+0WfV1ZxO52Xrq//Xm202pisZ44VmzJihyMhIj1/oe++9V7/73e+UlZWll156Sdu2bdN9992nqqqqBu2/Llcyvptuukm//e1v9e677+r3v/+93G63br31Vn3zzTeSWt8x3L17tw4cOKCJEyd6LG8ux/BKXOrv0OVy6ezZsw3ye9+c/OpXv9Lp06f1wx/+0FwWFxenjIwMZWZmatmyZcrLy9Ptt9+uU6dONWGn9dOlSxelp6frj3/8o/74xz8qKipKd911l/bu3SupYf7dak6OHj2qDRs2XPQ32ByPodvtVkpKin7wgx/o5ptvvmRdc3kvbPVfsYGmN2/ePK1cuVJbt271uKB4zJgx5n/37dtX/fr10/e+9z1t3bpVd999d1O0Wm/x8fEeX9x76623qnfv3vrf//1fvfDCC03YWeN488031bdvXw0ePNhjeUs+hlayYsUKzZkzR++++67HNTT33Xef+d/9+vVTXFycunfvrtWrV2vChAlN0Wq93XTTTbrpppvMn2+99VZ9+eWXWrBggf7v//6vCTtrHMuXL1doaKhGjhzpsbw5HsPk5GQdOHCgya438xZnhK5Sp06d5Ofnp8LCQo/lhYWFioiIqPU5ERERl62v/l9vttmYrmSM1X71q19p3rx5+uCDD9SvX7/L1l5//fXq1KmTvvjii6vu2RtXM75qAQEB+v73v2/23pqOYWlpqVauXFmvf1Sb6hheiUv9HdrtdgUHBzfI70VzsHLlSk2cOFGrV6++6GOIC4WGhurGG29sEcevNoMHDzZ7by3HTzo/c+q3v/2tHn30UdlstsvWNvUxnDJlitatW6e//OUv6tq162Vrm8t7IUHoKtlsNsXGxiorK8tc5na7lZWV5XHGoKb4+HiPeknatGmTWR8dHa2IiAiPGpfLpV27dl1ym43pSsYonb/a/4UXXlBmZqYGDRpU536++eYbfffdd+rSpUuD9F1fVzq+mqqqqrR//36z99ZyDKXz01vLysr04x//uM79NNUxvBJ1/R02xO9FU/vDH/6gcePG6Q9/+IPHbQ8u5fTp0/ryyy9bxPGrTW5urtl7azh+1bZt26YvvviiXv9npKmOoWEYmjJlit555x1t2bJF0dHRdT6n2bwXNthl1xa2cuVKIzAw0MjIyDA+/fRTY9KkSUZoaKjhdDoNwzCMRx991Jg5c6ZZv2PHDsPf39/41a9+ZXz22WfG7NmzjYCAAGP//v1mzbx584zQ0FDj3XffNT755BPjgQceMKKjo42zZ89e8/EZhvdjnDdvnmGz2Yz/9//+n3Hs2DHzcerUKcMwDOPUqVPGU089ZWRnZxt5eXnG5s2bjYEDBxo33HCDce7cuWY/vjlz5hgbN240vvzySyMnJ8cYM2aMERQUZBw8eNCsaenHsNptt91mjB49+qLlze0Ynjp1yti3b5+xb98+Q5Lx6quvGvv27TO+/vprwzAMY+bMmcajjz5q1v/973832rRpYzz99NPGZ599ZixdutTw8/MzMjMzzZq6XrPmPL63337b8Pf3N5YuXerxN1hcXGzW/OxnPzO2bt1q5OXlGTt27DASEhKMTp06GUVFRc1+fAsWLDDWrl1rHDlyxNi/f7/x5JNPGr6+vsbmzZvNmuZ0/AzD+zFW+/GPf2zExcXVus3mcgwnT55shISEGFu3bvX4fTtz5oxZ01zfCwlCDeTXv/610a1bN8NmsxmDBw82PvzwQ3PdnXfeaSQlJXnUr1692rjxxhsNm81m9OnTx1i/fr3HerfbbTz77LNGeHi4ERgYaNx9993G4cOHr8VQLsmbMXbv3t2QdNFj9uzZhmEYxpkzZ4xhw4YZnTt3NgICAozu3bsbjz/+eJP9A2UY3o0vJSXFrA0PDzfuv/9+Y+/evR7ba+nH0DAM49ChQ4Yk44MPPrhoW83tGFZPp77wUT2mpKQk484777zoOQMGDDBsNptx/fXXG2+99dZF273ca3YteTu+O++887L1hnH+dgFdunQxbDab8W//9m/G6NGjjS+++OLaDuyfvB3fSy+9ZHzve98zgoKCjA4dOhh33XWXsWXLlou221yOn2Fc2e9ocXGxERwcbLz++uu1brO5HMPaxiXJ42+qub4X+vxzAAAAAJbDNUIAAMCyCEIAAMCyCEIAAMCyCEIAAMCyCEIAAMCyCEIAAMCyCEIAAMCyCEIAAMCyCEIAAMCyCEIAAMCyCEIAAMCyCEIAAMCy/j87zcqci8STdwAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#salesbycategory\n",
        "sales_by_category=df.groupby(\"Category\")[\"Sales\"].sum().reset_index().plot(kind=\"box\")\n",
        "print(sales_by_category)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 448
        },
        "id": "MNLl0G9ulmVJ",
        "outputId": "de7af644-0164-41e0-b374-80554283caef"
      },
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Axes(0.125,0.11;0.775x0.77)\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAkIAAAGdCAYAAAD+JxxnAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAyJElEQVR4nO3de3RU5b3/8U8uZBISc0FNhsQEAihUjCJyTGORtoccBhovHDyiaRYiREULFKQ/br/KxWM9gYBFxRu2FjgLq0CLaAPiCcEWwTRglEsA46UpIjCgwMyAkgCZ5/eHP/ZhJCLDxRie92utvVh7P9/9zHfvter+dGfvmQhjjBEAAICFIpu7AQAAgOZCEAIAANYiCAEAAGsRhAAAgLUIQgAAwFoEIQAAYC2CEAAAsBZBCAAAWCu6uRv4PgsGg9q1a5cuuugiRURENHc7AADgNBhjdPDgQaWnpysy8tT3fAhCp7Br1y5lZmY2dxsAAOAM7NixQ5dddtkpa8IKQo2NjZo6daoWLFggr9er9PR03X333XrooYeavGNy//33a86cOZo1a5ZGjx7tbN+/f79Gjhypv/zlL4qMjNRtt92mJ554QgkJCU7Npk2bNHz4cK1fv16XXnqpRo4cqXHjxoXMv3jxYk2aNEn//Oc/dfnll2v69On62c9+5owbYzRlyhT97ne/k8/n049+9CM9++yzuvzyy0/reC+66CJJX53IxMTEcE4VAABoJoFAQJmZmc51/JRMGB599FFz8cUXm7KyMlNXV2cWL15sEhISzBNPPHFS7ZIlS8w111xj0tPTzaxZs0LG+vbta6655hrz97//3bz11lumU6dOprCw0Bn3+/0mLS3NFBUVmZqaGvPSSy+ZuLg4M2fOHKdm7dq1JioqypSWlpqtW7eahx56yLRq1cps3rzZqZk2bZpJSkoyS5cuNRs3bjS33HKLyc7ONocPHz6t4/X7/UaS8fv94ZwmAADQjMK5focVhAoKCszQoUNDtg0YMMAUFRWFbPv0009NRkaGqampMe3atQsJQlu3bjWSzPr1651tr7/+uomIiDA7d+40xhjzzDPPmJSUFNPQ0ODUjB8/3nTu3NlZHzhwoCkoKAj53NzcXDNs2DBjjDHBYNC43W4zY8YMZ9zn8xmXy2Veeuml0zpeghAAAC1PONfvsN4au+GGG1RRUaEPPvhAkrRx40atWbNG/fr1c2qCwaAGDRqksWPHqmvXrifNUVlZqeTkZPXo0cPZlp+fr8jISFVVVTk1vXr1UkxMjFPj8XhUW1urAwcOODX5+fkhc3s8HlVWVkqS6urq5PV6Q2qSkpKUm5vr1HxdQ0ODAoFAyAIAAC5cYT0jNGHCBAUCAXXp0kVRUVFqbGzUo48+qqKiIqdm+vTpio6O1i9/+csm5/B6vUpNTQ1tIjpabdq0kdfrdWqys7NDatLS0pyxlJQUeb1eZ9uJNSfOceJ+TdV8XUlJiR5++OFTngMAAHDhCOuO0KJFi/Tiiy/qj3/8o959913Nnz9fM2fO1Pz58yVJ1dXVeuKJJzRv3rwW+br5xIkT5ff7nWXHjh3N3RIAADiPwrojNHbsWE2YMEF33nmnJCknJ0fbt29XSUmJBg8erLfeekt79+5VVlaWs09jY6N+9atf6fHHH9c///lPud1u7d27N2TeY8eOaf/+/XK73ZIkt9utPXv2hNQcX/+2mhPHj29r27ZtSE23bt2aPD6XyyWXyxXOKQEAAC1YWHeEvvzyy5O+mCgqKkrBYFCSNGjQIG3atEkbNmxwlvT0dI0dO1ZvvPGGJCkvL08+n0/V1dXOHKtWrVIwGFRubq5Ts3r1ah09etSpKS8vV+fOnZWSkuLUVFRUhPRSXl6uvLw8SVJ2drbcbndITSAQUFVVlVMDAAAsF85T2IMHDzYZGRnO6/NLliwxl1xyiRk3btw37vP1t8aM+er1+WuvvdZUVVWZNWvWmMsvvzzk9Xmfz2fS0tLMoEGDTE1NjXn55ZdN69atT3p9Pjo62sycOdNs27bNTJkypcnX55OTk82rr75qNm3aZG699VZenwcA4AJ33l6fDwQCZtSoUSYrK8vExsaaDh06mF//+tchr7l/XVNBaN++faawsNAkJCSYxMREM2TIEHPw4MGQmo0bN5qePXsal8tlMjIyzLRp006ae9GiReaKK64wMTExpmvXrmbZsmUh48Fg0EyaNMmkpaUZl8tlevfubWpra0/7eAlCAAC0POFcvyOMMaZ570l9fwUCASUlJcnv9/PN0gAAtBDhXL/59XkAAGAtghAAALAWQQgAAFgrrO8RAoDmdvhIoz7+7NBZz1N/tFGfHjisy1LiFNsq6hx0JnW8NEFxMedmLgDfDYIQgBbl488O6abZa5q7jSaVjeypqzKSmrsNAGEgCAFoUTpemqCykT3Pep6P9h7S6IUb9Pgd3dQpNeEcdPZVbwBaFoIQgBYlLibqnN516ZSawF0cwGI8LA0AAKxFEAIAANYiCAEAAGsRhAAAgLUIQgAAwFoEIQAAYC2CEAAAsBZBCAAAWIsgBAAArEUQAgAA1iIIAQAAaxGEAACAtQhCAADAWgQhAABgLYIQAACwFkEIAABYiyAEAACsRRACAADWIggBAABrEYQAAIC1CEIAAMBaBCEAAGAtghAAALAWQQgAAFiLIAQAAKxFEAIAANYiCAEAAGsRhAAAgLUIQgAAwFoEIQAAYC2CEAAAsBZBCAAAWIsgBAAArEUQAgAA1iIIAQAAaxGEAACAtQhCAADAWgQhAABgLYIQAACwFkEIAABYK6wg1NjYqEmTJik7O1txcXHq2LGjHnnkERljJElHjx7V+PHjlZOTo/j4eKWnp+uuu+7Srl27QubZv3+/ioqKlJiYqOTkZBUXF+vQoUMhNZs2bdKNN96o2NhYZWZmqrS09KR+Fi9erC5duig2NlY5OTlavnx5yLgxRpMnT1bbtm0VFxen/Px8ffjhh+EcMgAAuICFFYSmT5+uZ599Vk899ZS2bdum6dOnq7S0VLNnz5Ykffnll3r33Xc1adIkvfvuu1qyZIlqa2t1yy23hMxTVFSkLVu2qLy8XGVlZVq9erXuu+8+ZzwQCKhPnz5q166dqqurNWPGDE2dOlXPP/+8U/P222+rsLBQxcXFeu+999S/f3/1799fNTU1Tk1paamefPJJPffcc6qqqlJ8fLw8Ho/q6+vP6GQBAIALjAlDQUGBGTp0aMi2AQMGmKKiom/cZ926dUaS2b59uzHGmK1btxpJZv369U7N66+/biIiIszOnTuNMcY888wzJiUlxTQ0NDg148ePN507d3bWBw4caAoKCkI+Kzc31wwbNswYY0wwGDRut9vMmDHDGff5fMblcpmXXnrptI7X7/cbScbv959WPYCWY/OnPtNufJnZ/KmvuVsBcI6Fc/0O647QDTfcoIqKCn3wwQeSpI0bN2rNmjXq16/fN+7j9/sVERGh5ORkSVJlZaWSk5PVo0cPpyY/P1+RkZGqqqpyanr16qWYmBinxuPxqLa2VgcOHHBq8vPzQz7L4/GosrJSklRXVyev1xtSk5SUpNzcXKfm6xoaGhQIBEIWAABw4YoOp3jChAkKBALq0qWLoqKi1NjYqEcffVRFRUVN1tfX12v8+PEqLCxUYmKiJMnr9So1NTW0iehotWnTRl6v16nJzs4OqUlLS3PGUlJS5PV6nW0n1pw4x4n7NVXzdSUlJXr44Ye/9TwAAIALQ1h3hBYtWqQXX3xRf/zjH/Xuu+9q/vz5mjlzpubPn39S7dGjRzVw4EAZY/Tss8+es4bPp4kTJ8rv9zvLjh07mrslAABwHoV1R2js2LGaMGGC7rzzTklSTk6Otm/frpKSEg0ePNipOx6Ctm/frlWrVjl3gyTJ7XZr7969IfMeO3ZM+/fvl9vtdmr27NkTUnN8/dtqThw/vq1t27YhNd26dWvy+Fwul1wu1+mdDAAA0OKFdUfoyy+/VGRk6C5RUVEKBoPO+vEQ9OGHH2rlypW6+OKLQ+rz8vLk8/lUXV3tbFu1apWCwaByc3OdmtWrV+vo0aNOTXl5uTp37qyUlBSnpqKiImTu8vJy5eXlSZKys7PldrtDagKBgKqqqpwaAABguXCewh48eLDJyMgwZWVlpq6uzixZssRccsklZty4ccYYY44cOWJuueUWc9lll5kNGzaY3bt3O8uJb4D17dvXXHvttaaqqsqsWbPGXH755aawsNAZ9/l8Ji0tzQwaNMjU1NSYl19+2bRu3drMmTPHqVm7dq2Jjo42M2fONNu2bTNTpkwxrVq1Mps3b3Zqpk2bZpKTk82rr75qNm3aZG699VaTnZ1tDh8+fFrHy1tjwIWLt8aAC1c41++wglAgEDCjRo0yWVlZJjY21nTo0MH8+te/dkJOXV2dkdTk8uabbzrz7Nu3zxQWFpqEhASTmJhohgwZYg4ePBjyWRs3bjQ9e/Y0LpfLZGRkmGnTpp3Uz6JFi8wVV1xhYmJiTNeuXc2yZctCxoPBoJk0aZJJS0szLpfL9O7d29TW1p728RKEgAsXQQi4cIVz/Y4w5v9/LTROEggElJSUJL/fH/KcE4CWr2anXzfNXqOykT11VUZSc7cD4BwK5/rNb40BAABrEYQAAIC1CEIAAMBaBCEAAGAtghAAALAWQQgAAFiLIAQAAKxFEAIAANYiCAEAAGsRhAAAgLUIQgAAwFoEIQAAYC2CEAAAsBZBCAAAWIsgBAAArEUQAgAA1iIIAQAAaxGEAACAtQhCAADAWgQhAABgLYIQAACwFkEIAABYiyAEAACsRRACAADWIggBAABrEYQAAIC1CEIAAMBaBCEAAGAtghAAALAWQQgAAFiLIAQAAKxFEAIAANYiCAEAAGsRhAAAgLUIQgAAwFoEIQAAYC2CEAAAsBZBCAAAWIsgBAAArEUQAgAA1iIIAQAAaxGEAACAtQhCAADAWgQhAABgLYIQAACwFkEIAABYK6wg1NjYqEmTJik7O1txcXHq2LGjHnnkERljnBpjjCZPnqy2bdsqLi5O+fn5+vDDD0Pm2b9/v4qKipSYmKjk5GQVFxfr0KFDITWbNm3SjTfeqNjYWGVmZqq0tPSkfhYvXqwuXbooNjZWOTk5Wr58ecj46fQCAADsFVYQmj59up599lk99dRT2rZtm6ZPn67S0lLNnj3bqSktLdWTTz6p5557TlVVVYqPj5fH41F9fb1TU1RUpC1btqi8vFxlZWVavXq17rvvPmc8EAioT58+ateunaqrqzVjxgxNnTpVzz//vFPz9ttvq7CwUMXFxXrvvffUv39/9e/fXzU1NWH1AgAALGbCUFBQYIYOHRqybcCAAaaoqMgYY0wwGDRut9vMmDHDGff5fMblcpmXXnrJGGPM1q1bjSSzfv16p+b11183ERERZufOncYYY5555hmTkpJiGhoanJrx48ebzp07O+sDBw40BQUFIb3k5uaaYcOGnXYv38bv9xtJxu/3n1Y9gJZj86c+0258mdn8qa+5WwFwjoVz/Q7rjtANN9ygiooKffDBB5KkjRs3as2aNerXr58kqa6uTl6vV/n5+c4+SUlJys3NVWVlpSSpsrJSycnJ6tGjh1OTn5+vyMhIVVVVOTW9evVSTEyMU+PxeFRbW6sDBw44NSd+zvGa459zOr18XUNDgwKBQMgCAAAuXNHhFE+YMEGBQEBdunRRVFSUGhsb9eijj6qoqEiS5PV6JUlpaWkh+6WlpTljXq9XqampoU1ER6tNmzYhNdnZ2SfNcXwsJSVFXq/3Wz/n23r5upKSEj388MOncSYAAMCFIKw7QosWLdKLL76oP/7xj3r33Xc1f/58zZw5U/Pnzz9f/X2nJk6cKL/f7yw7duxo7pYAAMB5FNYdobFjx2rChAm68847JUk5OTnavn27SkpKNHjwYLndbknSnj171LZtW2e/PXv2qFu3bpIkt9utvXv3hsx77Ngx7d+/39nf7XZrz549ITXH17+t5sTxb+vl61wul1wu1+mdDAAA0OKFdUfoyy+/VGRk6C5RUVEKBoOSpOzsbLndblVUVDjjgUBAVVVVysvLkyTl5eXJ5/OpurraqVm1apWCwaByc3OdmtWrV+vo0aNOTXl5uTp37qyUlBSn5sTPOV5z/HNOpxcAAGC5cJ7CHjx4sMnIyDBlZWWmrq7OLFmyxFxyySVm3LhxTs20adNMcnKyefXVV82mTZvMrbfearKzs83hw4edmr59+5prr73WVFVVmTVr1pjLL7/cFBYWOuM+n8+kpaWZQYMGmZqaGvPyyy+b1q1bmzlz5jg1a9euNdHR0WbmzJlm27ZtZsqUKaZVq1Zm8+bNYfVyKrw1Bly4eGsMuHCFc/0OKwgFAgEzatQok5WVZWJjY02HDh3Mr3/965DX3IPBoJk0aZJJS0szLpfL9O7d29TW1obMs2/fPlNYWGgSEhJMYmKiGTJkiDl48GBIzcaNG03Pnj2Ny+UyGRkZZtq0aSf1s2jRInPFFVeYmJgY07VrV7Ns2bKQ8dPp5VQIQsCFiyAEXLjCuX5HGHPC10IjRCAQUFJSkvx+vxITE5u7HQDnUM1Ov26avUZlI3vqqoyk5m4HwDkUzvWb3xoDAADWIggBAABrEYQAAIC1CEIAAMBaBCEAAGAtghAAALAWQQgAAFiLIAQAAKxFEAIAANYiCAEAAGsRhAAAgLUIQgAAwFoEIQAAYC2CEAAAsBZBCAAAWIsgBAAArEUQAgAA1iIIAQAAaxGEAACAtQhCAADAWgQhAABgLYIQAACwFkEIAABYiyAEAACsFd3cDQCwQ93nX+iLhmPN3Ybjo72HQv79Pol3RSv7kvjmbgOwAkEIwHlX9/kX+unMvzZ3G00avXBDc7fQpDf/z08IQ8B3gCAE4Lw7fifo8Tu6qVNqQjN385X6o4369MBhXZYSp9hWUc3djuOjvYc0euGG79XdM+BCRhAC8J3plJqgqzKSmrsNR4/2zd0BgObGw9IAAMBaBCEAAGAtghAAALAWQQgAAFiLIAQAAKxFEAIAANYiCAEAAGsRhAAAgLUIQgAAwFoEIQAAYC2CEAAAsBZBCAAAWIsgBAAArEUQAgAA1iIIAQAAaxGEAACAtQhCAADAWgQhAABgrbCCUPv27RUREXHSMnz4cEmS1+vVoEGD5Ha7FR8fr+7du+vPf/5zyBz79+9XUVGREhMTlZycrOLiYh06dCikZtOmTbrxxhsVGxurzMxMlZaWntTL4sWL1aVLF8XGxionJ0fLly8PGTfGaPLkyWrbtq3i4uKUn5+vDz/8MJzDBQAAF7iwgtD69eu1e/duZykvL5ck3X777ZKku+66S7W1tXrttde0efNmDRgwQAMHDtR7773nzFFUVKQtW7aovLxcZWVlWr16te677z5nPBAIqE+fPmrXrp2qq6s1Y8YMTZ06Vc8//7xT8/bbb6uwsFDFxcV677331L9/f/Xv3181NTVOTWlpqZ588kk999xzqqqqUnx8vDwej+rr68/sTAEAgAuPOQujRo0yHTt2NMFg0BhjTHx8vPnv//7vkJo2bdqY3/3ud8YYY7Zu3WokmfXr1zvjr7/+uomIiDA7d+40xhjzzDPPmJSUFNPQ0ODUjB8/3nTu3NlZHzhwoCkoKAj5nNzcXDNs2DBjjDHBYNC43W4zY8YMZ9zn8xmXy2Veeuml0z4+v99vJBm/33/a+wA42eZPfabd+DKz+VNfc7fyvce5As5eONfvM35G6MiRI1qwYIGGDh2qiIgISdINN9yghQsXav/+/QoGg3r55ZdVX1+vn/zkJ5KkyspKJScnq0ePHs48+fn5ioyMVFVVlVPTq1cvxcTEODUej0e1tbU6cOCAU5Ofnx/Sj8fjUWVlpSSprq5OXq83pCYpKUm5ublODQAAQPSZ7rh06VL5fD7dfffdzrZFixbpjjvu0MUXX6zo6Gi1bt1ar7zyijp16iTpq2eIUlNTQxuIjlabNm3k9Xqdmuzs7JCatLQ0ZywlJUVer9fZdmLNiXOcuF9TNU1paGhQQ0ODsx4IBL71PAAAgJbrjO8IvfDCC+rXr5/S09OdbZMmTZLP59PKlSv1zjvvaMyYMRo4cKA2b958Tpo930pKSpSUlOQsmZmZzd0SAAA4j84oCG3fvl0rV67UPffc42z7+OOP9dRTT+kPf/iDevfurWuuuUZTpkxRjx499PTTT0uS3G639u7dGzLXsWPHtH//frndbqdmz549ITXH17+t5sTxE/drqqYpEydOlN/vd5YdO3ac3gkBAAAt0hkFoblz5yo1NVUFBQXOti+//PKrCSNDp4yKilIwGJQk5eXlyefzqbq62hlftWqVgsGgcnNznZrVq1fr6NGjTk15ebk6d+6slJQUp6aioiLkc8rLy5WXlydJys7OltvtDqkJBAKqqqpyapricrmUmJgYsgAAgAtX2EEoGAxq7ty5Gjx4sKKj//cRoy5duqhTp04aNmyY1q1bp48//liPPfaYysvL1b9/f0nSD37wA/Xt21f33nuv1q1bp7Vr12rEiBG68847nT+x/fznP1dMTIyKi4u1ZcsWLVy4UE888YTGjBnjfNaoUaO0YsUKPfbYY3r//fc1depUvfPOOxoxYoQkKSIiQqNHj9ZvfvMb51X+u+66S+np6U4vAAAAYb8+/8YbbxhJpra29qSxDz74wAwYMMCkpqaa1q1bm6uvvvqk1+n37dtnCgsLTUJCgklMTDRDhgwxBw8eDKnZuHGj6dmzp3G5XCYjI8NMmzbtpM9atGiRueKKK0xMTIzp2rWrWbZsWch4MBg0kyZNMmlpacblcpnevXs32fOp8Po8cG7wSvjp41wBZy+c63eEMcY0cxb73goEAkpKSpLf7+fPZMBZqNnp102z16hsZE9dlZHU3O18r3GugLMXzvWb3xoDAADWIggBAABrEYQAAIC1CEIAAMBaBCEAAGAtghAAALAWQQgAAFiLIAQAAKxFEAIAANYiCAEAAGsRhAAAgLUIQgAAwFoEIQAAYC2CEAAAsBZBCAAAWIsgBAAArEUQAgAA1iIIAQAAaxGEAACAtQhCAADAWgQhAABgLYIQAACwFkEIAABYiyAEAACsRRACAADWIggBAABrEYQAAIC1CEIAAMBaBCEAAGAtghAAALAWQQgAAFiLIAQAAKxFEAIAANYiCAEAAGsRhAAAgLUIQgAAwFoEIQAAYC2CEAAAsBZBCAAAWIsgBAAArEUQAgAA1iIIAQAAaxGEAACAtQhCAADAWgQhAABgLYIQAACwFkEIAABYK6wg1L59e0VERJy0DB8+3KmprKzUv/7rvyo+Pl6JiYnq1auXDh8+7Izv379fRUVFSkxMVHJysoqLi3Xo0KGQz9m0aZNuvPFGxcbGKjMzU6WlpSf1snjxYnXp0kWxsbHKycnR8uXLQ8aNMZo8ebLatm2ruLg45efn68MPPwzncAEAwAUurCC0fv167d6921nKy8slSbfffrukr0JQ37591adPH61bt07r16/XiBEjFBn5vx9TVFSkLVu2qLy8XGVlZVq9erXuu+8+ZzwQCKhPnz5q166dqqurNWPGDE2dOlXPP/+8U/P222+rsLBQxcXFeu+999S/f3/1799fNTU1Tk1paamefPJJPffcc6qqqlJ8fLw8Ho/q6+vP7EwBAIALjzkLo0aNMh07djTBYNAYY0xubq556KGHvrF+69atRpJZv369s+311183ERERZufOncYYY5555hmTkpJiGhoanJrx48ebzp07O+sDBw40BQUFIXPn5uaaYcOGGWOMCQaDxu12mxkzZjjjPp/PuFwu89JLL5328fn9fiPJ+P3+094HwMk2f+oz7caXmc2f+pq7le89zhVw9sK5fp/xM0JHjhzRggULNHToUEVERGjv3r2qqqpSamqqbrjhBqWlpenHP/6x1qxZ4+xTWVmp5ORk9ejRw9mWn5+vyMhIVVVVOTW9evVSTEyMU+PxeFRbW6sDBw44Nfn5+SH9eDweVVZWSpLq6urk9XpDapKSkpSbm+vUNKWhoUGBQCBkAQAAF64zDkJLly6Vz+fT3XffLUn6xz/+IUmaOnWq7r33Xq1YsULdu3dX7969nWdzvF6vUlNTQ+aJjo5WmzZt5PV6nZq0tLSQmuPr31Zz4viJ+zVV05SSkhIlJSU5S2Zm5umdDAAA0CKdcRB64YUX1K9fP6Wnp0uSgsGgJGnYsGEaMmSIrr32Ws2aNUudO3fWH/7wh3PT7Xk2ceJE+f1+Z9mxY0dztwQAAM6j6DPZafv27Vq5cqWWLFnibGvbtq0k6corrwyp/cEPfqBPPvlEkuR2u7V3796Q8WPHjmn//v1yu91OzZ49e0Jqjq9/W82J48e3He/r+Hq3bt2+8bhcLpdcLtcpjhwAAFxIzuiO0Ny5c5WamqqCggJnW/v27ZWenq7a2tqQ2g8++EDt2rWTJOXl5cnn86m6utoZX7VqlYLBoHJzc52a1atX6+jRo05NeXm5OnfurJSUFKemoqIi5HPKy8uVl5cnScrOzpbb7Q6pCQQCqqqqcmoAAADCDkLBYFBz587V4MGDFR39vzeUIiIiNHbsWD355JP605/+pI8++kiTJk3S+++/r+LiYklf3R3q27ev7r33Xq1bt05r167ViBEjdOeddzp/Yvv5z3+umJgYFRcXa8uWLVq4cKGeeOIJjRkzxvmsUaNGacWKFXrsscf0/vvva+rUqXrnnXc0YsQIp5fRo0frN7/5jV577TVt3rxZd911l9LT09W/f/+zOV8AAOBCEu4raW+88YaRZGpra5scLykpMZdddplp3bq1ycvLM2+99VbI+L59+0xhYaFJSEgwiYmJZsiQIebgwYMhNRs3bjQ9e/Y0LpfLZGRkmGnTpp30OYsWLTJXXHGFiYmJMV27djXLli0LGQ8Gg2bSpEkmLS3NuFwu07t372/s+Zvw+jxwbvBK+OnjXAFnL5zrd4QxxjRzFvveCgQCSkpKkt/vV2JiYnO3A7RYNTv9umn2GpWN7KmrMpKau53vNc4VcPbCuX7zW2MAAMBaBCEAAGAtghAAALAWQQgAAFiLIAQAAKxFEAIAANYiCAEAAGsRhAAAgLUIQgAAwFoEIQAAYC2CEAAAsBZBCAAAWIsgBAAArEUQAgAA1iIIAQAAaxGEAACAtQhCAADAWgQhAABgLYIQAACwFkEIAABYiyAEAACsRRACAADWIggBAABrEYQAAIC1CEIAAMBaBCEAAGAtghAAALAWQQgAAFiLIAQAAKxFEAIAANYiCAEAAGsRhAAAgLUIQgAAwFoEIQAAYC2CEAAAsBZBCAAAWIsgBAAArEUQAgAA1iIIAQAAaxGEAACAtQhCAADAWgQhAABgLYIQAACwFkEIAABYK7q5GwBw4WtorFdk7E7VBWoVGZvQ3O18r9UFDikydqcaGuslJTV3O8AFjyAE4Lzb9cV2xWfP1v9d19ydtAzx2dKuL7rpOqU1dyvABS+sINS+fXtt3779pO2/+MUv9PTTTzvrxhj97Gc/04oVK/TKK6+of//+ztgnn3yiBx54QG+++aYSEhI0ePBglZSUKDr6f1v561//qjFjxmjLli3KzMzUQw89pLvvvjvkM59++mnNmDFDXq9X11xzjWbPnq3rr7/eGa+vr9evfvUrvfzyy2poaJDH49EzzzyjtDT+wwJ819Lj2+mLupF64o5u6pjKHaFT+XjvIY1auEHpP23X3K0AVggrCK1fv16NjY3Oek1Njf7t3/5Nt99+e0jd448/roiIiJP2b2xsVEFBgdxut95++23t3r1bd911l1q1aqX/+q//kiTV1dWpoKBA999/v1588UVVVFTonnvuUdu2beXxeCRJCxcu1JgxY/Tcc88pNzdXjz/+uDwej2pra5WamipJevDBB7Vs2TItXrxYSUlJGjFihAYMGKC1a9eGd4YAnDVXVKyC9RnKTuysKy/mzz2nEqz3K1j/mVxRsc3dCmAHcxZGjRplOnbsaILBoLPtvffeMxkZGWb37t1GknnllVecseXLl5vIyEjj9Xqdbc8++6xJTEw0DQ0Nxhhjxo0bZ7p27RryOXfccYfxeDzO+vXXX2+GDx/urDc2Npr09HRTUlJijDHG5/OZVq1amcWLFzs127ZtM5JMZWXlaR+f3+83kozf7z/tfQCcbPOnPtNufJnZ/KmvuVv53uNcAWcvnOv3Gb81duTIES1YsEBDhw517v58+eWX+vnPf66nn35abrf7pH0qKyuVk5MT8ucpj8ejQCCgLVu2ODX5+fkh+3k8HlVWVjqfW11dHVITGRmp/Px8p6a6ulpHjx4NqenSpYuysrKcmqY0NDQoEAiELAAA4MJ1xkFo6dKl8vl8Ic/uPPjgg7rhhht06623NrmP1+s96Rmd4+ter/eUNYFAQIcPH9bnn3+uxsbGJmtOnCMmJkbJycnfWNOUkpISJSUlOUtmZuY3nwAAANDinXEQeuGFF9SvXz+lp6dLkl577TWtWrVKjz/++Lnq7Ts3ceJE+f1+Z9mxY0dztwQAAM6jMwpC27dv18qVK3XPPfc421atWqWPP/5YycnJio6Odt4Cu+222/STn/xEkuR2u7Vnz56QuY6vH/9T2jfVJCYmKi4uTpdccomioqKarDlxjiNHjsjn831jTVNcLpcSExNDFgAAcOE6oyA0d+5cpaamqqCgwNk2YcIEbdq0SRs2bHAWSZo1a5bmzp0rScrLy9PmzZu1d+9eZ7/y8nIlJibqyiuvdGoqKipCPq+8vFx5eXmSpJiYGF133XUhNcFgUBUVFU7Nddddp1atWoXU1NbW6pNPPnFqAAAAwv5CxWAwqLlz52rw4MEh3/3jdrubvNuSlZWl7OxsSVKfPn105ZVXatCgQSotLZXX69VDDz2k4cOHy+VySZLuv/9+PfXUUxo3bpyGDh2qVatWadGiRVq2bJkz55gxYzR48GD16NFD119/vR5//HF98cUXGjJkiCQpKSlJxcXFGjNmjNq0aaPExESNHDlSeXl5+uEPfxjuIQMAgAtU2EFo5cqV+uSTTzR06NCwPywqKkplZWV64IEHlJeXp/j4eA0ePFj/+Z//6dRkZ2dr2bJlevDBB/XEE0/osssu0+9//3vnO4Qk6Y477tBnn32myZMny+v1qlu3blqxYkXIA9SzZs1SZGSkbrvttpAvVAQAADguwhhjmruJ76tAIKCkpCT5/X6eFwLOQs1Ov26avUZlI3vqqgy+UPFUOFfA2Qvn+s2vzwMAAGsRhAAAgLUIQgAAwFoEIQAAYC2CEAAAsBZBCAAAWIsgBAAArEUQAgAA1iIIAQAAaxGEAACAtQhCAADAWgQhAABgLYIQAACwFkEIAABYiyAEAACsRRACAADWIggBAABrEYQAAIC1CEIAAMBaBCEAAGCt6OZuAMCF7/DRRklSzU5/M3fyv+qPNurTA4d1WUqcYltFNXc7jo/2HmruFgCrEIQAnHcf//+L+4Qlm5u5k5Yj3sV/noHvAv9LA3De9enqliR1TE1Q3Pfk7stHew9p9MINevyObuqUmtDc7YSId0Ur+5L45m4DsAJBCMB51yY+Rnden9XcbTSpU2qCrspIau42ADQTHpYGAADWIggBAABrEYQAAIC1CEIAAMBaBCEAAGAtghAAALAWQQgAAFiLIAQAAKxFEAIAANYiCAEAAGsRhAAAgLUIQgAAwFoEIQAAYC2CEAAAsBZBCAAAWIsgBAAArEUQAgAA1iIIAQAAaxGEAACAtQhCAADAWgQhAABgLYIQAACwFkEIAABYK6wg1L59e0VERJy0DB8+XPv379fIkSPVuXNnxcXFKSsrS7/85S/l9/tD5vjkk09UUFCg1q1bKzU1VWPHjtWxY8dCav7617+qe/fucrlc6tSpk+bNm3dSL08//bTat2+v2NhY5ebmat26dSHj9fX1Gj58uC6++GIlJCTotttu0549e8I5XAAAcIELKwitX79eu3fvdpby8nJJ0u23365du3Zp165dmjlzpmpqajRv3jytWLFCxcXFzv6NjY0qKCjQkSNH9Pbbb2v+/PmaN2+eJk+e7NTU1dWpoKBAP/3pT7VhwwaNHj1a99xzj9544w2nZuHChRozZoymTJmid999V9dcc408Ho/27t3r1Dz44IP6y1/+osWLF+tvf/ubdu3apQEDBpzxiQIAABcgcxZGjRplOnbsaILBYJPjixYtMjExMebo0aPGGGOWL19uIiMjjdfrdWqeffZZk5iYaBoaGowxxowbN8507do1ZJ477rjDeDweZ/366683w4cPd9YbGxtNenq6KSkpMcYY4/P5TKtWrczixYudmm3bthlJprKy8rSPz+/3G0nG7/ef9j4AWobNn/pMu/FlZvOnvuZuBcA5Fs71+4yfETpy5IgWLFigoUOHKiIioskav9+vxMRERUdHS5IqKyuVk5OjtLQ0p8bj8SgQCGjLli1OTX5+fsg8Ho9HlZWVzudWV1eH1ERGRio/P9+pqa6u1tGjR0NqunTpoqysLKemKQ0NDQoEAiELAAC4cJ1xEFq6dKl8Pp/uvvvuJsc///xzPfLII7rvvvucbV6vNyQESXLWvV7vKWsCgYAOHz6szz//XI2NjU3WnDhHTEyMkpOTv7GmKSUlJUpKSnKWzMzMbz4BAACgxYs+0x1feOEF9evXT+np6SeNBQIBFRQU6Morr9TUqVPPpr/v1MSJEzVmzBhnPRAIEIaA75nDRxr18WeHznqej/YeCvn3XOh4aYLiYqLO2XwAzr8zCkLbt2/XypUrtWTJkpPGDh48qL59++qiiy7SK6+8olatWjljbrf7pLe7jr/J5Xa7nX+//nbXnj17lJiYqLi4OEVFRSkqKqrJmhPnOHLkiHw+X8hdoRNrmuJyueRyuU7jDABoLh9/dkg3zV5zzuYbvXDDOZurbGRPXZWRdM7mA3D+nVEQmjt3rlJTU1VQUBCyPRAIyOPxyOVy6bXXXlNsbGzIeF5enh599FHt3btXqampkqTy8nIlJibqyiuvdGqWL18esl95ebny8vIkSTExMbruuutUUVGh/v37S5KCwaAqKio0YsQISdJ1112nVq1aqaKiQrfddpskqba2Vp988okzD4CWqeOlCSob2fOs56k/2qhPDxzWZSlxim11bu7idLw04ZzMA+A7FO6T2I2NjSYrK8uMHz/+pCe0c3NzTU5Ojvnoo4/M7t27neXYsWPGGGOOHTtmrrrqKtOnTx+zYcMGs2LFCnPppZeaiRMnOvP84x//MK1btzZjx44127ZtM08//bSJiooyK1ascGpefvll43K5zLx588zWrVvNfffdZ5KTk0PeRrv//vtNVlaWWbVqlXnnnXdMXl6eycvLC+tYeWsMAICWJ5zrd9hB6I033jCSTG1tbcj2N99800hqcqmrq3Pq/vnPf5p+/fqZuLg4c8kll5hf/epXzuv1J87VrVs3ExMTYzp06GDmzp17Uh+zZ882WVlZJiYmxlx//fXm73//e8j44cOHzS9+8QuTkpJiWrdubf793//d7N69O6xjJQgBANDyhHP9jjDGmGa6GfW9FwgElJSU5HwNAAAA+P4L5/rNb40BAABrEYQAAIC1CEIAAMBaBCEAAGAtghAAALAWQQgAAFiLIAQAAKxFEAIAANYiCAEAAGsRhAAAgLUIQgAAwFrRzd3A99nxn2ELBALN3AkAADhdx6/bp/NzqgShUzh48KAkKTMzs5k7AQAA4Tp48KCSkpJOWcOvz59CMBjUrl27dNFFFykiIqK52wFwDgUCAWVmZmrHjh3f+uvUAFoWY4wOHjyo9PR0RUae+ikgghAAKwUCASUlJcnv9xOEAIvxsDQAALAWQQgAAFiLIATASi6XS1OmTJHL5WruVgA0I54RAgAA1uKOEAAAsBZBCAAAWIsgBAAArEUQAmCtefPmKTk5ubnbANCMCEIAWqzPPvtMDzzwgLKysuRyueR2u+XxeLR27drmbg1AC8FvjQFosW677TYdOXJE8+fPV4cOHbRnzx5VVFRo3759zd0agBaCO0IAWiSfz6e33npL06dP109/+lO1a9dO119/vSZOnKhbbrlFkvTb3/5WOTk5io+PV2Zmpn7xi1/o0KFDp5z31VdfVffu3RUbG6sOHTro4Ycf1rFjxyR99ftFU6dOde5Apaen65e//OV5P1YA5w9BCECLlJCQoISEBC1dulQNDQ1N1kRGRurJJ5/Uli1bNH/+fK1atUrjxo37xjnfeust3XXXXRo1apS2bt2qOXPmaN68eXr00UclSX/+8581a9YszZkzRx9++KGWLl2qnJyc83J8AL4bfKEigBbrz3/+s+69914dPnxY3bt3149//GPdeeeduvrqq5us/9Of/qT7779fn3/+uaSvHpYePXq0fD6fJCk/P1+9e/fWxIkTnX0WLFigcePGadeuXfrtb3+rOXPmqKamRq1atTrvxwfg/CMIAWjR6uvr9dZbb+nvf/+7Xn/9da1bt06///3vdffdd2vlypUqKSnR+++/r0AgoGPHjqm+vl5ffPGFWrdufVIQuvTSS3Xo0CFFRUU58zc2Njr77Nu3Tz/60Y9kjFHfvn31s5/9TDfffLOio3ncEmipCEIALij33HOPysvL9be//U1dunTRAw88oDvuuENt2rTRmjVrVFxcrAMHDig5OfmkIBQXF6eHH35YAwYMOGneDh06KDIyUocPH9bKlStVXl6uxYsXKzs7W3/729+4QwS0UPzfGAAXlCuvvFJLly5VdXW1gsGgHnvsMUVGfvU45KJFi065b/fu3VVbW6tOnTp9Y01cXJxuvvlm3XzzzRo+fLi6dOmizZs3q3v37uf0OAB8NwhCAFqkffv26fbbb9fQoUN19dVX66KLLtI777yj0tJS3XrrrerUqZOOHj2q2bNn6+abb9batWv13HPPnXLOyZMn66abblJWVpb+4z/+Q5GRkdq4caNqamr0m9/8RvPmzVNjY6Nyc3PVunVrLViwQHFxcWrXrt13dNQAzjXeGgPQIiUkJCg3N1ezZs1Sr169dNVVV2nSpEm699579dRTT+maa67Rb3/7W02fPl1XXXWVXnzxRZWUlJxyTo/Ho7KyMv3P//yP/uVf/kU//OEPNWvWLCfoJCcn63e/+51+9KMf6eqrr9bKlSv1l7/8RRdffPF3ccgAzgOeEQIAANbijhAAALAWQQgAAFiLIAQAAKxFEAIAANYiCAEAAGsRhAAAgLUIQgAAwFoEIQAAYC2CEAAAsBZBCAAAWIsgBAAArEUQAgAA1vp/SFUoyQqlFMMAAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#monthlysales\n",
        "monthly_sales=df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum().reset_index()\n",
        "print(monthly_sales)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "-KDEGEZ_mKDZ",
        "outputId": "aa7305ce-9450-4c99-d1e5-e0dcadb2d493"
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   Order Date        Sales\n",
            "0     2014-01   14236.8950\n",
            "1     2014-02    4519.8920\n",
            "2     2014-03   55691.0090\n",
            "3     2014-04   28295.3450\n",
            "4     2014-05   23648.2870\n",
            "5     2014-06   34595.1276\n",
            "6     2014-07   33946.3930\n",
            "7     2014-08   27909.4685\n",
            "8     2014-09   81777.3508\n",
            "9     2014-10   31453.3930\n",
            "10    2014-11   78628.7167\n",
            "11    2014-12   69545.6205\n",
            "12    2015-01   18174.0756\n",
            "13    2015-02   11951.4110\n",
            "14    2015-03   38726.2520\n",
            "15    2015-04   34195.2085\n",
            "16    2015-05   30131.6865\n",
            "17    2015-06   24797.2920\n",
            "18    2015-07   28765.3250\n",
            "19    2015-08   36898.3322\n",
            "20    2015-09   64595.9180\n",
            "21    2015-10   31404.9235\n",
            "22    2015-11   75972.5635\n",
            "23    2015-12   74919.5212\n",
            "24    2016-01   18542.4910\n",
            "25    2016-02   22978.8150\n",
            "26    2016-03   51715.8750\n",
            "27    2016-04   38750.0390\n",
            "28    2016-05   56987.7280\n",
            "29    2016-06   40344.5340\n",
            "30    2016-07   39261.9630\n",
            "31    2016-08   31115.3743\n",
            "32    2016-09   73410.0249\n",
            "33    2016-10   59687.7450\n",
            "34    2016-11   79411.9658\n",
            "35    2016-12   96999.0430\n",
            "36    2017-01   43971.3740\n",
            "37    2017-02   20301.1334\n",
            "38    2017-03   58872.3528\n",
            "39    2017-04   36521.5361\n",
            "40    2017-05   44261.1102\n",
            "41    2017-06   52981.7257\n",
            "42    2017-07   45264.4160\n",
            "43    2017-08   63120.8880\n",
            "44    2017-09   87866.6520\n",
            "45    2017-10   77776.9232\n",
            "46    2017-11  118447.8250\n",
            "47    2017-12   83829.3188\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#monthlysales\n",
        "monthly_sales=df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum().reset_index().plot(kind=\"box\")\n",
        "print(monthly_sales)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 448
        },
        "id": "eLnnYFH1n1Sd",
        "outputId": "085946d1-60f0-4a9a-91eb-b9dd184a74f9"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Axes(0.125,0.11;0.775x0.77)\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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O3EAX8kVFaO2pgFKdQ/RsL78uud82pr8amv6XK6orvU/JIGuKuR3jd10002qqanRzp07ncfYsWOVm5vr/N89e/ZUeXm5857a2lrt379fGRkZkqSMjAzV1NQE3d1VVlYmt9utYcOGOTOn76N9pn0f0dHRGjNmTNBMW1ubysvLnRkAAGC3kF8R6t27t0aMGBH0WlxcnPr27eu8npeXp6KiIvXp00dut1szZ85URkaGrrnmGknShAkTNGzYMP385z9XSUmJfD6fHnzwQeXn5ztXbO677z499dRTmj17tu666y5t2rRJa9eu1fr1653jFhUVaerUqRo7dqzGjRunJ598UsePH9e0adNCfdoAAKAL6rS7xs7niSeeUGRkpG677TY1NzcrKytLy5cvd7ZHRUWptLRUM2bMUEZGhuLi4jR16lT967/+qzOTmpqq9evX6/7779eSJUt08cUX6/e//72ysrKcmUmTJunzzz/X/Pnz5fP5NGrUKL366qtnfYEaAADYKcIYY8K9iO+qQCAgj8cjv98vt9sd7uUAXdaug37dsuxtlc4crxED+I7Q+fCzAr65jnx+87fGAACAtQghAABgLUIIAABYixACAADWIoQAAIC1CCEAAGAtQggAAFiLEAIAANYihAAAgLUIIQAAYC1CCAAAWIsQAgAA1iKEAACAtQghAABgLUIIAABYixACAADWIoQAAIC1CCEAAGAtQggAAFiLEAIAANYihAAAgLUIIQAAYK0e4V4AgO7vREurJGnXQX+YV/L/NLW06rOjJ3RxYqxiekaFezmOj+sbw70EwCqEEIBO99f//8P9V/9VE+aVdB1xLv7rGfg28P9pADrdhOFeSdJl/eIV+x25+vJxfaMK1+zUk5NGaXC/+HAvJ0icq4dSL4oL9zIAKxBCADpdn7hoTR43MNzLOKfB/eI1YoAn3MsAECZ8WRoAAFiLEAIAANYihAAAgLUIIQAAYC1CCAAAWIsQAgAA1iKEAACAtQghAABgLUIIAABYixACAADWIoQAAIC1CCEAAGAtQggAAFiLEAIAANYihAAAgLUIIQAAYC1CCAAAWIsQAgAA1iKEAACAtQghAABgLUIIAABYixACAADWCnkIFRcX6/vf/7569+6tfv36KScnR7W1tUEzTU1Nys/PV9++fRUfH6/bbrtNdXV1QTP79+9Xdna2evXqpX79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ERHxLawWwLclEAgoJSVFBw4ckNvtDvdyAISQMUbHjh1TcnLy1852+xCaNGmSPv/8c82fP18+n0+jRo3Sq6++etYXqM8lMjJSF1988bewSgDh4na7CSGgG/q6K0HtIsyF/AINALqZQCAgj8cjv99PCAEW464xAABgLUIIgJVcLpceeuihoDtFAdiHX40BAABrcUUIAABYixACAADWIoQAAIC1CCEA1lq1apUSEhLCvQwAYUQIAeiyPv/8c82YMUMDBw6Uy+WS1+tVVlaW3nnnnXAvDUAX0e3/ZWkA3ddtt92mkydPavXq1br00ktVV1en8vJyHT58ONxLA9BFcEUIQJfU0NCgt956S4899phuvPFGDRo0SOPGjdPcuXP14x//WJL0+OOPKy0tTXFxcUpJSdEvfvELNTY2nne/f/7znzV69GjFxMTo0ksv1cMPP6xTp05J+vLvFy1YsMC5ApWcnKxf/vKXnX6uADoPIQSgS4qPj1d8fLxeeuklNTc3n3MmMjJSS5cu1e7du7V69Wpt2rRJs2fP/sp9vvXWW7rzzjs1a9Ys7dmzR88++6xWrVqlRx55RJL0pz/9SU888YSeffZZ7d27Vy+99JLS0tI65fwAfDv4BxUBdFl/+tOfNH36dJ04cUKjR4/WDTfcoMmTJ+uqq6465/x//ud/6r777tMXX3wh6csvSxcWFqqhoUGSlJmZqZtuuklz58513vOHP/xBs2fP1qFDh/T444/r2Wef1a5du9SzZ89OPz8AnY8QAtClNTU16a233tK7776rjRs3auvWrfr973+vf/7nf9brr7+u4uJiffTRRwoEAjp16pSampp0/Phx9erV66wQ+t73vqfGxkZFRUU5+29tbXXec/jwYV177bUyxujmm2/Wj370I02cOFE9evB1S6CrIoQAdCt33323ysrKtHnzZg0dOlQzZszQpEmT1KdPH7399tvKy8vT0aNHlZCQcFYIxcbG6uGHH9att9561n4vvfRSRUZG6sSJE3r99ddVVlamdevWKTU1VZs3b+YKEdBF8T9jAHQrw4YN00svvaTq6mq1tbVp8eLFioz88uuQa9euPe97R48erdraWg0ePPgrZ2JjYzVx4kRNnDhR+fn5Gjp0qGpqajR69OiQngeAbwchBKBLOnz4sH72s5/prrvu0lVXXaXevXtr+/btKikp0T/+4z9q8ODBamlp0bJlyzRx4kS98847WrFixXn3OX/+fN1yyy0aOHCgfvrTnyoyMlLvv/++du3apYULF2rVqlVqbW1Venq6evXqpT/84Q+KjY3VoEGDvqWzBhBq3DUGoEuKj49Xenq6nnjiCV1//fUaMWKE5s2bp+nTp+upp57SyJEj9fjjj+uxxx7TiBEj9Mc//lHFxcXn3WdWVpZKS0v13//93/r+97+va665Rk888YQTOgkJCfrd736na6+9VldddZVef/11vfLKK+rbt++3ccoAOgHfEQIAANbiihAAALAWIQQAAKxFCAEAAGsRQgAAwFqEEAAAsBYhBAAArEUIAQAAaxFCAADAWoQQAACwFiEEAACsRQgBAABrEUIAAMBa/x/EVUGvQQohMAAAAABJRU5ErkJggg==\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#monthlysales\n",
        "monthly_sales=df.groupby(df['Order Date'].dt.to_period('M'))['Sales'].sum().reset_index().plot(kind=\"area\")\n",
        "print(monthly_sales)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 448
        },
        "id": "d7R6cOgVrTlt",
        "outputId": "3be582d3-22c2-4cdb-ad64-ba718c700406"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Axes(0.125,0.11;0.775x0.77)\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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FhZKdY8yld1ux+eff44nn3wSN954Iy666CJcffXVmDt3Lv7t3/4NAPDMM8/giiuuwMCBAzF8+HDce++96OjoiLvfd999F2PHjkVOTg6+9a1v4ZFHHoHf7wfQXSNowYIF0ghUYWEhfvvb3xr+WomIKPnerTqN2W9VweM3f9cFxTlCO3fuxI033ij9LAYnd911FxYsWID33nsPAHDVVVeFPe7TTz/F97//fQDAihUrMHPmTNx0001SQcUlS5ZI2+bl5WHDhg0oLS3FuHHjcN5552HevHlSDSEAuPbaa7Fy5Uo89NBD+OMf/4iRI0di7dq1Ug0hAJgzZw5cLhdmzJgBu92O66+/HuvXr8/42jTnnHMOzjnnHKxduxbXXHMN+vXr12ObXr16YcmSJRgxYgSOHTuGe++9F3PmzMGLL74YdZ+ff/457rzzTixZsgTf/e53cfToUenzmj9/Pt555x08++yzePPNN/Htb38bNpsNX331laGvk4iIUuPZskM40dKJUefn4j+/+61UH05cWYIgCKk+CLNyOp3Iy8uDw+HoMU3mdrtx/PhxjBgxIiyw2nvagVue/yLZh4p1912P0d/Mk739O++8g+nTp6Orqwtjx47F9773Pdx+++248soro27/9ttv49e//jWam5sB9EyWLi4uxk033YS5c+dKj3n99dcxZ84c1NXV4ZlnnsHLL7+MvXv3om/fvnGPLdZ7S0RE1nDFgo/R7vbjR1cU4MWp45L+/PHO35HYvyBDTZkyBXV1dXjvvfdw880347PPPsPYsWOxfPlyAMAnn3yCm266Cd/85jcxaNAg/OpXv0JLS0vMvmpfffUVHn30UWm06ZxzzsH06dOlXmw/+9nP0NXVhW9961uYPn061qxZI02bERFR+vAFgmh3d3+/Nzo9CbZOPQZCGSwnJwf/+q//iocffhhbt27Ff/zHf2D+/Pk4ceIEbrnlFlx55ZV45513UFlZiaVLlwKAlOsVqaOjA4888oiUP1ZVVYU9e/bg8OHDyMnJwfDhw1FdXY0XX3wR/fv3x7333osbbrghLCGeiIisL3QVc0sSa+qpxe7zJBk1ahTWrl2LyspKBINBPP3001LT07feeivuY8eOHYvq6mpccsklMbfp378/br31Vtx6660oLS3FZZddhj179mDs2LG6vg4iIkqd1s6zwY+ji4EQmVBLSwt+9rOf4Z577sGVV16JQYMGYefOnVi0aBF+/OMf45JLLoHP58Pzzz+PW2+9FV9++SWWLVsWd5/z5s3DLbfcggsvvBC33XYbevXqha+++gp79+7F448/juXLlyMQCGDChAkYMGAAXn/9dfTv3x8XXXRRkl41ERElQ2vIKJDLY/5VY5wa09nggdno1ye5b2u/Pr0weGB24g3POOecczBhwgQ8++yzuOGGGzB69Gg8/PDDmD59Ol544QWMGTMGzzzzDJ588kmMHj0aK1aswMKFC+Pus6SkBOvWrcOGDRvwne98B9dccw2effZZKdDJz8/HX//6V1x33XW48sor8cknn+D999/vUWeKiIisLTQQ8gaSW2BYDa4ai0PNqjGAvca04qoxIiLr+r/yE3j43X3Szwcfuxk5fXsn9RiUrBrj1JgBvpnfP60CEyIiIrlaXeGLYOrsXfjWN85J0dEkxqkxIiIi0k2rK3zJ/NHG+F0JUo2BEBEREemmtTN8ROh4sytFRyIPAyEiIiLSTWSObE1b9EK8ZsFASCPmmuuP7ykRkXVFFlGsd7hTdCTyMBBSSeyXFavlBKknvqeJepIREZH5RI4INbWbu80GV42p1Lt3b+Tn56OxsREAMGDAAGRlZaX4qKxNEAR0dnaisbER+fn56N07ucstiYhIG0EQwuoIAT0DI7NhIKRBQUEBAEjBEOkjPz9fem+JiMg6XN5AjyKKji5z95RkIKRBVlYWzj//fAwdOpTNQ3XSt29fjgQREVlUtNGfLp+522wwENJB7969efImIqKMFzktBgC+gABBEEybPsJkaSIiItJFaOf5UB0ef5KPRD4GQkRERKSL1o7uQChy7KemxbwrrBkIERERkS7axBGhiEjoiInbbDAQIiIiIl1IOUIRdXFPtJi3zQYDISIiItKFGAhF9gc41daV/IORiYEQERER6SLaqjEAsDnN22aDgRARERHpoi3GqrHmDvO22WAgRERERLqIbLgqsrvMW3SYgRARERHpItbUmNPDQIiIiIjSWCAowNEZPeBx+4JRbzcDBkJERESkmb3T22O1mCgQFBAMxro3tRgIERERkWaxEqVFrS5zJkwzECIiIiLNWhMkRB83aVFFBkJERESkWaIRn6ONDISIiIgoTYkjQpENV0U1rQyEiIiIKE0lyhE6bdI2GwyEiIiISLNYfcZENieTpYmI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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#monthlyprofits\n",
        "monthly_profits=df.groupby(df['Order Date'].dt.to_period('M'))['Profit'].sum().reset_index()\n",
        "print(monthly_profits)\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VXQItxFXrYuT",
        "outputId": "4b02d753-849f-41b5-aedc-0826dfc22bfb"
      },
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   Order Date      Profit\n",
            "0     2014-01   2450.1907\n",
            "1     2014-02    862.3084\n",
            "2     2014-03    498.7299\n",
            "3     2014-04   3488.8352\n",
            "4     2014-05   2738.7096\n",
            "5     2014-06   4976.5244\n",
            "6     2014-07   -841.4826\n",
            "7     2014-08   5318.1050\n",
            "8     2014-09   8328.0994\n",
            "9     2014-10   3448.2573\n",
            "10    2014-11   9292.1269\n",
            "11    2014-12   8983.5699\n",
            "12    2015-01  -3281.0070\n",
            "13    2015-02   2813.8508\n",
            "14    2015-03   9732.0978\n",
            "15    2015-04   4187.4962\n",
            "16    2015-05   4667.8690\n",
            "17    2015-06   3335.5572\n",
            "18    2015-07   3288.6483\n",
            "19    2015-08   5355.8084\n",
            "20    2015-09   8209.1627\n",
            "21    2015-10   2817.3660\n",
            "22    2015-11  12474.7884\n",
            "23    2015-12   8016.9659\n",
            "24    2016-01   2824.8233\n",
            "25    2016-02   5004.5795\n",
            "26    2016-03   3611.9680\n",
            "27    2016-04   2977.8149\n",
            "28    2016-05   8662.1464\n",
            "29    2016-06   4750.3781\n",
            "30    2016-07   4432.8779\n",
            "31    2016-08   2062.0693\n",
            "32    2016-09   9328.6576\n",
            "33    2016-10  16243.1425\n",
            "34    2016-11   4011.4075\n",
            "35    2016-12  17885.3093\n",
            "36    2017-01   7140.4391\n",
            "37    2017-02   1613.8720\n",
            "38    2017-03  14751.8915\n",
            "39    2017-04    933.2900\n",
            "40    2017-05   6342.5828\n",
            "41    2017-06   8223.3357\n",
            "42    2017-07   6952.6212\n",
            "43    2017-08   9040.9557\n",
            "44    2017-09  10991.5556\n",
            "45    2017-10   9275.2755\n",
            "46    2017-11   9690.1037\n",
            "47    2017-12   8483.3468\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "monthly_profits=df.groupby(df['Order Date'].dt.to_period('M'))['Profit'].sum().reset_index().plot(kind=\"box\")\n",
        "print(monthly_profits)\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 448
        },
        "id": "NptjSB7TKqu3",
        "outputId": "57d887c9-073d-4838-c2a7-bbcf6eb01dfe"
      },
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Axes(0.125,0.11;0.775x0.77)\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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BwAoksgBAIokcgCAIokcAKBIIgcAKJLIAQCKJHIAgCKJHACgSCIHACiSyAEAiiRyAIAiiRwAoEgiBwAoksgBAIokcgCAIg2u9QAAW721eUuee3V9v+zr2TXr+/z5cR0waniGNgzql30BO4fIAXYZz726Pp+/+v5+3ecFNy3rl/0sOP+oHLpPS7/sC9g5RA6wyzhg1PAsOP+oftnXxre35KU338q+I4emacjHPwNzwKjh/TAVsDOJHGCXMbRhUL+eLTli/37bFTAAufAYACiSyAEAiiRyAIAiiRwAoEgiBwAoksgBAIokcgCAIokcAKBIIgcAKJLIAQCKJHIAgCKJHACgSCIHACjSbv1byCuVSpKkp6enxpMAAB/V1tftra/j72e3jpx169YlSTo6Omo8CQCwvdatW5eWlpb33V5X+bAMKlhvb29eeeWV7Lnnnqmrq6v1OEA/6unpSUdHR1588cU0NzfXehygH1Uqlaxbty7t7e2pr3//K29268gBytXT05OWlpZ0d3eLHNhNufAYACiSyAEAiiRygCI1Njbma1/7WhobG2s9ClAjrskBAIrkTA4AUCSRAwAUSeQAAEUSOcBuZe7cuWltbU1dXV1uu+22nHnmmZk+fXqtxwJ2ABceA7ukM888Mz/4wQ+SJEOGDMl+++2XL3/5y/nqV7+awYN/s99I89RTT2XChAn5yU9+kiOPPDIjR47Mxo0bU6lUMmLEiCTJ0UcfncMPPzxXXXVVPx0JUCu79e+uAnZt06ZNyw033JBNmzbljjvuyHnnnZchQ4Zkzpw5fdZt3rw5DQ0NH7q/5557LknyhS98ofqrXHzEHMrl7Spgl9XY2Ji2traMGTMm5557bqZMmZKf/vSn1beY/vZv/zbt7e0ZP358kuSJJ57I5z73uQwdOjSf/OQnc84552T9+vVJfv021Yknnpgkqa+vr0bOu9+uOvPMM3Pvvfdm/vz5qaurS11dXZ5//vmdftxA/xA5wIAxdOjQbN68OUmyaNGirFixIgsXLsyCBQuyYcOGTJ06NSNHjsyjjz6aW265JT/72c8ya9asJMlFF12UG264IUmyatWqrFq16j37nz9/fjo7O3P22WdX13R0dOy8AwT6lbergF1epVLJokWLctddd+X888/Pq6++mmHDhuV73/te9W2qf/zHf8zGjRvzwx/+MMOGDUuSXHPNNTnxxBPzrW99K62trdXrbtra2rb5PC0tLWloaMgee+zxvmuAgcOZHGCXtWDBggwfPjxNTU05/vjjc8opp2Tu3LlJkokTJ/a5Duepp57KYYcdVg2cJPn93//99Pb2ZsWKFTt7dGAX4EwOsMs65phj8g//8A9paGhIe3t7n09VvTtmALbFmRxglzVs2LCMGzcu++2334d+bPzggw/O448/ng0bNlTve+CBB1JfX1+9MPmjaGhoyJYtW37jmYFdh8gBinD66aenqakpZ5xxRpYvX5677747559/fr70pS+ltbX1I+9n//33z8MPP5znn38+r732Wnp7e3fg1MCOJHKAIuyxxx6566678sYbb+R3f/d3c/LJJ+fYY4/NNddcs137ueiiizJo0KBMmDAho0aNygsvvLCDJgZ2ND/xGAAokjM5AECRRA4AUCSRAwAUSeQAAEUSOQBAkUQOAFAkkQMAFEnkAABFEjkAQJFEDgBQJJEDABRJ5AAARfp/xdKArm6s1q0AAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "monthly_profits=df.groupby(df['Order Date'].dt.to_period('M'))['Profit'].sum().reset_index().plot(kind=\"hist\")\n",
        "print(monthly_profits)\n",
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 448
        },
        "id": "vqYcHGYKK0EG",
        "outputId": "4c6f0718-f95d-4ca3-80b1-1cadf681a0b0"
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Axes(0.125,0.11;0.775x0.77)\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "iVBORw0KGgoAAAANSUhEUgAAAjIAAAGdCAYAAAAIbpn/AAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/bCgiHAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAlsElEQVR4nO3de3RU5aH+8WdIMpMEScItNw0kyq0kiOCFg2CXSI4QKQXtOaJFDZSDttIKRlRyKiBaDeCRBVUK9pxKpK2grAJ1KeLBCFIVuQuiHC4SbpIQ5JIbJoTM+/vDxfycJoQwDNnzxu9nrVnL2fudnWfmXSGP7+w94zLGGAEAAFiohdMBAAAAAkWRAQAA1qLIAAAAa1FkAACAtSgyAADAWhQZAABgLYoMAACwFkUGAABYK9zpAJeb1+vVkSNH1KpVK7lcLqfjAACARjDGqLy8XMnJyWrR4vzrLs2+yBw5ckQpKSlOxwAAAAE4dOiQrrrqqvPub/ZFplWrVpK+eyFiYmIcTgMAABqjrKxMKSkpvr/j59Psi8y5t5NiYmIoMgAAWOZCp4Vwsi8AALAWRQYAAFiLIgMAAKzV7M+RAQAgGIwxOnv2rGpra52O0iyEhYUpPDz8kj8ahSIDAMAFnDlzRkVFRTp9+rTTUZqV6OhoJSUlye12B3wMigwAAA3wer0qLCxUWFiYkpOT5Xa7+YDVS2SM0ZkzZ3Ts2DEVFhaqc+fODX7oXUMoMgAANODMmTPyer1KSUlRdHS003GajaioKEVEROjAgQM6c+aMIiMjAzoOJ/sCANAIga4Y4PyC8ZoyKwAAwFoUGQAAYC1Hz5FZu3atXnjhBW3evFlFRUVatmyZhg8fLkmqqanRU089pRUrVmjfvn2KjY1VZmampk+fruTkZCdjAwAgSUqd9E6T/rz904c06c87n6efflrz5s1TSUmJli1bpuXLl+vUqVNavnx5k2dxdEWmsrJSPXv21Ny5c+vsO336tLZs2aLJkydry5YtWrp0qXbt2qWf/vSnDiQFAMA+o0aNksvlksvlktvtVqdOnfTMM8/o7NmzAR9z586dmjZtml555RUVFRUpKytLc+bMUX5+vm/MrbfeqgkTJlz6E2gER1dksrKylJWVVe++2NhYrVq1ym/byy+/rJtuukkHDx5Uhw4dmiIiAABWGzx4sBYsWKDq6mqtWLFC48aNU0REhHJzc/3GnTlzplGf5/LVV19JkoYNG+a7DN3j8QQ/eCNZdY5MaWmpXC6X4uLizjumurpaZWVlfjcAAH6oPB6PEhMT1bFjR/3qV79SZmam3nrrLY0aNUrDhw/Xc889p+TkZHXt2lWS9Pnnn+u2225TVFSU2rZtqwcffFAVFRWSvntLaejQoZK+u+LoXJE5d6xz//3hhx9qzpw5vtWg/fv3X7bnZ83nyFRVVenJJ5/Uvffeq5iYmPOOy8vL07Rp05owGVC/pn7vPBhC5f13AJdPVFSUjh8/LkkqKChQTEyM7x2QyspKDRo0SH379tXGjRtVUlKi//iP/9Cvf/1r5efna+LEiUpNTdXo0aNVVFRU7/HnzJmj3bt3KyMjQ88884wkqX379pft+VixIlNTU6O7775bxhjNmzevwbG5ubkqLS313Q4dOtREKQEACF3GGL3//vt67733dNttt0mSWrZsqf/5n/9Renq60tPT9frrr6uqqkoLFy5URkaGbrvtNr388sv685//rKNHj+qKK67wvSuSmJioxMTEOj8nNjZWbrdb0dHRvjFhYWGX7XmFfJE5V2IOHDigVatWNbgaI323hBYTE+N3AwDgh+rtt9/WFVdcocjISGVlZWnEiBF6+umnJUk9evTwOy9m586d6tmzp1q2bOnb1q9fP3m9Xu3ataupozdKSL+1dK7E7NmzR6tXr1bbtm2djgQAgFUGDBigefPmye12Kzk5WeHh//9P//cLi60cLTIVFRXau3ev735hYaE+++wztWnTRklJSfq3f/s3bdmyRW+//bZqa2tVXFwsSWrTps0lfVMmAAA/FC1btlSnTp0aNfZHP/qR8vPzVVlZ6Ss5H3/8sVq0aOE7Gbgx3G63amtrA8p7sRx9a2nTpk3q1auXevXqJUnKyclRr169NGXKFH399dd66623dPjwYV133XVKSkry3T755BMnYwMA0CyNHDlSkZGRys7O1o4dO7R69Wr95je/0f3336+EhIRGHyc1NVXr16/X/v379c0338jr9V62zI6uyNx6660yxpx3f0P7AABwWnO70i86Olrvvfeexo8frxtvvFHR0dH62c9+plmzZl3UcSZOnKjs7Gx1795d3377rQoLC5WamnpZMrtMM28LZWVlio2NVWlpKSf+oklx+TXQPFRVVamwsFBpaWmKjIx0Ok6z0tBr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JRWZTZs26eGHH1ZSUpJmzZqliRMn6quvvtKqVat05MgRDRs2LFg5AQAA6ggP5EGzZs3SggULtGvXLt1xxx1auHCh7rjjDrVo8V0vSktLU35+vlJTU4OZFQAAwE9ARWbevHn6xS9+oVGjRikpKaneMfHx8frTn/50SeEAAAAaElCR2bNnzwXHuN1uZWdnB3J4AACARgnoHJkFCxZoyZIldbYvWbJEr7322iWHAgAAaIyAikxeXp7atWtXZ3t8fLyef/75Sw4FAADQGAEVmYMHDyotLa3O9o4dO+rgwYOXHAoAAKAxAioy8fHx2r59e53t27ZtU9u2bS85FAAAQGMEVGTuvfdePfLII1q9erVqa2tVW1urDz74QOPHj9c999wT7IwAAAD1CuiqpWeffVb79+/XwIEDFR7+3SG8Xq8eeOABzpEBAABNJqAi43a79cYbb+jZZ5/Vtm3bFBUVpR49eqhjx47BzgcAAHBeARWZc7p06aIuXboEKwsAAMBFCajI1NbWKj8/XwUFBSopKZHX6/Xb/8EHHwQlHAAAQEMCKjLjx49Xfn6+hgwZooyMDLlcrmDnAgAAuKCAiszixYv15ptv6o477gh2HgAAgEYL6PJrt9utTp06BTsLAADARQmoyDz22GOaM2eOjDHBzgMAANBoAb219NFHH2n16tV69913lZ6eroiICL/9S5cuDUo4AACAhgRUZOLi4nTnnXcGOwsAAMBFCajILFiwINg5AAAALlpA58hI0tmzZ/X+++/rlVdeUXl5uSTpyJEjqqioCFo4AACAhgS0InPgwAENHjxYBw8eVHV1tf71X/9VrVq10owZM1RdXa358+cHOycAAEAdAa3IjB8/XjfccINOnjypqKgo3/Y777xTBQUFQQsHAADQkIBWZP7xj3/ok08+kdvt9tuempqqr7/+OijBAAAALiSgFRmv16va2to62w8fPqxWrVpdcigAAIDGCKjI3H777Zo9e7bvvsvlUkVFhaZOncrXFgAAgCYT0FtLL774ogYNGqTu3burqqpKP//5z7Vnzx61a9dOixYtCnZGAACAegVUZK666ipt27ZNixcv1vbt21VRUaExY8Zo5MiRfif/AgAAXE4BFRlJCg8P13333RfMLAAAABcloCKzcOHCBvc/8MADAYUBAAC4GAEVmfHjx/vdr6mp0enTp+V2uxUdHU2R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p5vY2FizfPlys23bNvPTn/7UpKWlmW+//dY3ZvDgwaZnz57m008/Nf/4xz9Mp06dzL333uvbX1paahISEszIkSPNjh07zKJFi0xUVJR55ZVXfGM+/vhjExYWZmbOnGm+/PJL89RTT5mIiAjz+eefX/bXwBYXmqvs7GwzePBgv9+zEydO+I1hrpxFkUHQ3HTTTWbcuHG++7W1tSY5Odnk5eU5mKr5mjp1qunZs2e9+06dOmUiIiLMkiVLfNt27txpJJl169YZY777B7xFixamuLjYN2bevHkmJibGVFdXG2OMeeKJJ0x6errfsUeMGGEGDRoU5GfTfP3zH0ev12sSExPNCy+84Nt26tQp4/F4zKJFi4wxxnz55ZdGktm4caNvzLvvvmtcLpf5+uuvjTHG/OEPfzCtW7f2zZUxxjz55JOma9euvvt33323GTJkiF+ePn36mIceeiioz7G5OF+RGTZs2Hkfw1w5j7eWEBRnzpzR5s2blZmZ6dvWokULZWZmat26dQ4ma9727Nmj5ORkXX311Ro5cqQOHjwoSdq8ebNqamr85qNbt27q0KGDbz7WrVunHj16+H245KBBg1RWVqYvvvjCN+b7xzg3hjkNXGFhoYqLi/1e19jYWPXp08dvbuLi4nTDDTf4xmRmZqpFixZav369b8yPf/xjud1u35hBgwZp165dOnnypG8M83fp1qxZo/j4eHXt2lW/+tWvdPz4cd8+5sp5FBkExTfffKPa2to6n7ickJCg4uJih1I1b3369FF+fr5WrlypefPmqbCwULfccovKy8tVXFwst9td5wtTvz8fxcXF9c7XuX0NjSkrK9O33357mZ5Z83butW3od6W4uFjx8fF++8PDw9WmTZugzB+/k403ePBgLVy4UAUFBZoxY4Y+/PBDZWVlqba2VhJzFQpC/isKANQvKyvL99/XXnut+vTpo44dO+rNN99UVFSUg8mA5uOee+7x/XePHj107bXX6pprrtGaNWs0cOBAB5PhHFZkEBTt2rVTWFhYnatijh49qsTERIdS/bDExcWpS5cu2rt3rxITE3XmzBmdOnXKb8z35yMxMbHe+Tq3r6ExMTExlKUAnXttG/pdSUxMVElJid/+s2fP6sSJE0GZP34nA3f11VerXbt22rt3ryTmKhRQZBAUbrdb119/vQoKCnzbvF6vCgoK1LdvXweT/XBUVFToq6++UlJSkq6//npFRET4zceuXbt08OBB33z07dtXn3/+ud8/wqtWrVJMTIy6d+/uG/P9Y5wbw5wGLi0tTYmJiX6va1lZmdavX+83N6dOndLmzZt9Yz744AN5vV716dPHN2bt2rWqqanxjVm1apW6du2q1q1b+8Ywf8F1+PBhHT9+XElJSZKYq5Dg9NnGaD4WL15sPB6Pyc/PN19++aV58MEHTVxcnN9VMQiexx57zKxZs8YUFhaajz/+2GRmZpp27dqZkpISY8x3l1936NDBfPDBB2bTpk2mb9++pm/fvr7Hn7v8+vbbbzefffaZWblypWnfvn29l18//vjjZufOnWbu3Llcft0I5eXlZuvWrWbr1q1Gkpk1a5bZunWrOXDggDHmu8uv4+LizN///nezfft2M2zYsHovv+7Vq5dZv369+eijj0znzp39Luk9deqUSUhIMPfff7/ZsWOHWbx4sYmOjq5zSW94eLj5r//6L7Nz504zdepULun9Jw3NVXl5uZk4caJZt26dKSwsNO+//77p3bu36dy5s6mqqvIdg7lyFkUGQfXSSy+ZDh06GLfbbW666Sbz6aefOh2p2RoxYoRJSkoybrfbXHnllWbEiBFm7969vv3ffvutefjhh03r1q1NdHS0ufPOO01RUZHfMfbv32+ysrJMVFSUadeunXnsscdMTU2N35jVq1eb6667zrjdbnP11VebBQsWNMXTs9rq1auNpDq37OxsY8x3l2BPnjzZJCQkGI/HYwYOHGh27drld4zjx4+be++911xxxRUmJibGjB492pSXl/uN2bZtm+nfv7/xeDzmyiuvNNOnT6+T5c033zRdunQxbrfbpKenm3feeeeyPW8bNTRXp0+fNrfffrtp3769iYiIMB07djRjx46t8z9nzJWzXMYY48xaEAAAwKXhHBkAAGAtigwAALAWRQYAAFiLIgMAAKxFkQEAANaiyAAAAGtRZAAAgLUoMgAAwFoUGQAAYC2KDAAAsBZFBgAAWIsiAwAArPX/AB0uwvw5+BZzAAAAAElFTkSuQmCC\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#profitanalysisbycategory\n",
        "profit_analysis=df.groupby('Category')['Profit'].sum().reset_index()\n",
        "print(profit_analysis)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ynI-ecO8LVbh",
        "outputId": "f83b3d57-9871-4b75-e043-e2c60cec5274"
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "          Category       Profit\n",
            "0        Furniture   18451.2728\n",
            "1  Office Supplies  122490.8008\n",
            "2       Technology  145454.9481\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#profitanalysisbycategory\n",
        "profit_analysis=df.groupby('Category')['Profit'].sum().reset_index().plot(kind=\"bar\")\n",
        "print(profit_analysis)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 443
        },
        "id": "f-8yggRlL2_i",
        "outputId": "8c0b34ca-7c5b-4acf-a6a8-21a77fe56a94"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Axes(0.125,0.11;0.775x0.77)\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#profitanalysisbycategory\n",
        "profit_analysis=df.groupby('Category')['Profit'].sum().reset_index().plot(kind=\"area\")\n",
        "print(profit_analysis)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 448
        },
        "id": "BZ7KzgcFMYho",
        "outputId": "8bcb94e9-29e4-4c8e-e119-0055c55090f2"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Axes(0.125,0.11;0.775x0.77)\n"
          ]
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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jYiLi5Nq5HIkR4mNcecBcMJEIiIiOZn9jFBoaCh27dqFr7/+Gn379pWux3F3d4erqyvc3d0REhKC8PBw9O/fH25ubli4cCH8/PwwYcIEAMDEiRMxcuRIzJo1CxEREVAqlVi5ciVCQ0OlMzavvPIKPvroI7z++ut46aWXcPToUezbtw+HDh2SegkPD0dwcDDGjRuH8ePH48MPP4RWq8XcuXPNPewOefqBuzF2SD+kXqrihIlEREQyMvvt8w4OrX8y1vbt2zFnzhwATRMqLlmyBLt370ZDQwMCAgLw8ccfm7xldenSJSxYsADHjh1Dnz59EBwcjPXr16Nnz/9mt2PHjuHVV1/FmTNncM899+DNN9+U9tHso48+wjvvvAOlUokxY8Zg06ZN8PX1bddYuvL2+e9zlJj/eapZt0lERGSN5Lx9vsvnEbJmXRmEfjhTipc/SzHrNomIiKyRTc8jRERERGSpGISIiIjIbjEIERERkd1iECIiIiK7xSBEREREdotBiIiIiOwWgxARERHZLQYhIiIislsMQkRERGS3GISIiIjIbjEIERERkd1iECIiIiK7xSBEREREdotBiIiIiOwWgxARERHZLQYhIiIislsMQkRERGS3GISIiIjIbjEIERERkd1iECIiIiK7xSBEREREdotBiIiIiOwWgxARERHZLQYhIiIislsMQkRERGS3GISIiIjIbjEIERERkd1iECIiIiK7xSBEREREdotBiIiIiOwWgxARERHZLQYhIiIislsMQkRERGS3GISIiIjIbjEIERERkd1iECIiIiK7xSBEREREdssugtDmzZtx3333wcXFBb6+vkhKSpK7JSIiIrIANh+E9u7di/DwcKxevRppaWkYPXo0AgICUFZWJndrREREJDObD0Lvv/8+5s2bh7lz52LkyJGIjIxE7969sW3bNrlbIyIiIpn1lLuBrtTY2IjU1FSsWLFCWubo6Ah/f38kJCS0qG9oaEBDQ4P0tVqtBgBoNBqz96atqYaxodbs2yUiIrI25n6dbd6eEKLNWpsOQteuXYPBYICnp6fJck9PT+Tm5raoX7duHdauXdtiube3d5f1SEREZO/cP+ya7VZXV8Pd3f22NTYdhDpqxYoVCA8Pl742Go2orKzEgAED4ODgYNZ9aTQaeHt7o7i4GG5ubmbdtiWw9fEBtj9Gjs/62foYOT7r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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df.columns"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CUZsZqDENGLA",
        "outputId": "168460f0-8e2b-46e3-85fd-33322115ebbc"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "Index(['Row ID', 'Order ID', 'Order Date', 'Ship Date', 'Ship Mode',\n",
              "       'Customer ID', 'Customer Name', 'Segment', 'Country', 'City', 'State',\n",
              "       'Postal Code', 'Region', 'Product ID', 'Category', 'Sub-Category',\n",
              "       'Product Name', 'Sales', 'Quantity', 'Discount', 'Profit'],\n",
              "      dtype='object')"
            ]
          },
          "metadata": {},
          "execution_count": 30
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "df['Category'].value_counts().plot(kind=\"pie\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 424
        },
        "id": "XwhvJJFANMR6",
        "outputId": "2b59ec04-9b1e-4ed5-9531-0e6b799cce9f"
      },
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "<Axes: ylabel='Category'>"
            ]
          },
          "metadata": {},
          "execution_count": 32
        },
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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rtd3cHCoeX6gesallZUVjh07Biur2qvSG2LCChEpD4tNoby8vHDq1KlatyUmJtYqLH2xtbWFWq2+4/WB6kOb7u7uNa9/P23btoVarUZ2djYefPBBvWclIuXj5BGFevjhh3H06FGsWrUKaWlpmD179h1Fpy/BwcE4efIkUlNTcfPmTVRWViIsLAyBgYGYM2cO0tLS8OOPP2Lx4sX3fa6IiAjExcVh1KhR2LhxI9LT03H48GH8+9//xo8//miQ/ESkLCw2herbty9mzpyJN954Ax06dMDt27cxatQog7zWuHHj0Lx5c8TGxsLLywv79u2DjY0N1q5di7NnzyI6OhqLFi3C/Pnz6/V88fHxGDVqFCZPnozmzZtjyJAhOHLkiN7P7xGRMnHlESIiUhSO2IiISFFYbEREpCgsNiIiUhQWGxERKQqLjYiIFIXFRkREisJiIyIiRWGxERGRorDYiIhIUVhsRESkKCw2IiJSFBYbEREpCouNiIgUhcVGRESKwmIjIiJFYbEREZGisNiIiEhRWGxERKQoLDYiIlIUFhsRESkKi42IiBSFxUZERIrCYiMiIkVhsRERkaKw2IiISFFYbEREpCgsNiIiUhQWGxERKQqLjYiIFIXFRkREisJiIyIiRWGxERGRovw/vEa1JwiYT38AAAAASUVORK5CYII=\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "5qwAZBz2OOva"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}