{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3db452b9-cb6d-4293-a9ed-e1fb98f6d8e5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: dash in c:\\users\\soonn\\appdata\\roaming\\jupyterlab-desktop\\jlab_server\\lib\\site-packages (3.0.4)\n",
      "Requirement already satisfied: Flask<3.1,>=1.0.4 in c:\\users\\soonn\\appdata\\roaming\\jupyterlab-desktop\\jlab_server\\lib\\site-packages (from dash) (3.0.3)\n",
      "Requirement already satisfied: Werkzeug<3.1 in c:\\users\\soonn\\appdata\\roaming\\jupyterlab-desktop\\jlab_server\\lib\\site-packages (from dash) (3.0.6)\n",
      "Requirement already satisfied: plotly>=5.0.0 in c:\\users\\soonn\\appdata\\roaming\\jupyterlab-desktop\\jlab_server\\lib\\site-packages (from dash) (6.1.2)\n",
      "Requirement already satisfied: importlib-metadata in c:\\users\\soonn\\appdata\\roaming\\jupyterlab-desktop\\jlab_server\\lib\\site-packages (from dash) (8.4.0)\n",
      "Requirement already satisfied: typing-extensions>=4.1.1 in c:\\users\\soonn\\appdata\\roaming\\jupyterlab-desktop\\jlab_server\\lib\\site-packages (from dash) (4.13.2)\n",
      "Requirement already satisfied: requests in c:\\users\\soonn\\appdata\\roaming\\jupyterlab-desktop\\jlab_server\\lib\\site-packages (from dash) (2.32.3)\n",
      "Requirement already satisfied: retrying in c:\\users\\soonn\\appdata\\roaming\\jupyterlab-desktop\\jlab_server\\lib\\site-packages (from dash) (1.3.4)\n",
      "Requirement already satisfied: nest-asyncio in c:\\users\\soonn\\appdata\\roaming\\jupyterlab-desktop\\jlab_server\\lib\\site-packages (from dash) (1.6.0)\n",
      "Requirement already satisfied: setuptools in c:\\users\\soonn\\appdata\\roaming\\jupyterlab-desktop\\jlab_server\\lib\\site-packages (from dash) (72.2.0)\n",
      "Requirement already satisfied: Jinja2>=3.1.2 in c:\\users\\soonn\\appdata\\roaming\\jupyterlab-desktop\\jlab_server\\lib\\site-packages (from Flask<3.1,>=1.0.4->dash) (3.1.4)\n",
      "Requirement already satisfied: itsdangerous>=2.1.2 in c:\\users\\soonn\\appdata\\roaming\\jupyterlab-desktop\\jlab_server\\lib\\site-packages (from Flask<3.1,>=1.0.4->dash) (2.2.0)\n",
      "Requirement already satisfied: click>=8.1.3 in c:\\users\\soonn\\appdata\\roaming\\jupyterlab-desktop\\jlab_server\\lib\\site-packages (from Flask<3.1,>=1.0.4->dash) (8.2.1)\n",
      "Requirement already satisfied: blinker>=1.6.2 in c:\\users\\soonn\\appdata\\roaming\\jupyterlab-desktop\\jlab_server\\lib\\site-packages (from Flask<3.1,>=1.0.4->dash) (1.9.0)\n",
      "Requirement already satisfied: narwhals>=1.15.1 in c:\\users\\soonn\\appdata\\roaming\\jupyterlab-desktop\\jlab_server\\lib\\site-packages (from plotly>=5.0.0->dash) (1.41.0)\n",
      "Requirement already satisfied: packaging in c:\\users\\soonn\\appdata\\roaming\\jupyterlab-desktop\\jlab_server\\lib\\site-packages (from plotly>=5.0.0->dash) (24.2)\n",
      "Requirement already satisfied: MarkupSafe>=2.1.1 in c:\\users\\soonn\\appdata\\roaming\\jupyterlab-desktop\\jlab_server\\lib\\site-packages (from Werkzeug<3.1->dash) (2.1.5)\n",
      "Requirement already satisfied: zipp>=0.5 in c:\\users\\soonn\\appdata\\roaming\\jupyterlab-desktop\\jlab_server\\lib\\site-packages (from importlib-metadata->dash) (3.20.1)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\soonn\\appdata\\roaming\\jupyterlab-desktop\\jlab_server\\lib\\site-packages (from requests->dash) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\soonn\\appdata\\roaming\\jupyterlab-desktop\\jlab_server\\lib\\site-packages (from requests->dash) (3.8)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\soonn\\appdata\\roaming\\jupyterlab-desktop\\jlab_server\\lib\\site-packages (from requests->dash) (2.4.0)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\soonn\\appdata\\roaming\\jupyterlab-desktop\\jlab_server\\lib\\site-packages (from requests->dash) (2025.4.26)\n",
      "Requirement already satisfied: six>=1.7.0 in c:\\users\\soonn\\appdata\\roaming\\jupyterlab-desktop\\jlab_server\\lib\\site-packages (from retrying->dash) (1.16.0)\n",
      "Requirement already satisfied: colorama in c:\\users\\soonn\\appdata\\roaming\\jupyterlab-desktop\\jlab_server\\lib\\site-packages (from click>=8.1.3->Flask<3.1,>=1.0.4->dash) (0.4.6)\n"
     ]
    }
   ],
   "source": [
    "!pip install dash"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "e9707fac-dbc0-4eb2-9102-ea1b25a93060",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "from dash import Dash, html"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4424d9b0-f4a0-4f4e-a7cd-af6b4df4b417",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Dash()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "641dc4f9-3598-46ca-8640-2545cd440b67",
   "metadata": {},
   "outputs": [],
   "source": [
    "app.layout = html.Div('My Dashboard')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "f8384a99-ed90-4d14-8a65-7edad55c4ad4",
   "metadata": {},
   "outputs": [
    {
     "ename": "ObsoleteAttributeException",
     "evalue": "app.run_server has been replaced by app.run",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mObsoleteAttributeException\u001b[0m                Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[5], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;18m__name__\u001b[39m \u001b[38;5;241m==\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;124m__main__\u001b[39m\u001b[38;5;124m'\u001b[39m:\n\u001b[1;32m----> 2\u001b[0m     \u001b[43mapp\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mrun_server\u001b[49m(debug \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mTrue\u001b[39;00m)\n",
      "File \u001b[1;32m\\\\?\\C:\\Users\\soonn\\AppData\\Roaming\\jupyterlab-desktop\\jlab_server\\Lib\\site-packages\\dash\\_obsolete.py:22\u001b[0m, in \u001b[0;36mObsoleteChecker.__getattr__\u001b[1;34m(self, name)\u001b[0m\n\u001b[0;32m     20\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m name \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_obsolete_attributes:\n\u001b[0;32m     21\u001b[0m     err \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_obsolete_attributes[name]\n\u001b[1;32m---> 22\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m err\u001b[38;5;241m.\u001b[39mexc(err\u001b[38;5;241m.\u001b[39mmessage)\n\u001b[0;32m     23\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[38;5;28mgetattr\u001b[39m(\u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m\u001b[38;5;18m__dict__\u001b[39m, name)\n",
      "\u001b[1;31mObsoleteAttributeException\u001b[0m: app.run_server has been replaced by app.run"
     ]
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "    app.run_server(debug = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c6400dd6-4266-404e-8afa-fc1389d7403e",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
