# KAFKA CLUSTERS

### An ETL data pipeline to extract vocal data, transform and load it to a database using Kafka clusters for a text to speech conversion project

![](screenshots/image-I.png)

## Project details

10 Academy Batch 6 - Weekly Challenge: Week 6 - Data Engineering: text-to-speech data collection with Kafka, Airflow, and Spark

**Table of contents**

- [Introduction](#introduction)
- [Overview](#overview)
- [Objective](#objective)
- [Requirements](#requirements)
- [Install](#install)
- [How to use the](#examples)
- [End-to-end pipelines](#pipelines)
- [Notebooks](#notebooks)
- [Scripts](#scripts)
- [Test](#test)
- [Authors](#authors)

## Introduction

> Data is everywhere. In order to get the best out of it one needs to extract it from several sources, make required transformations and load it to a data warehouse for further analysis and explorations. This is where ETL data pipelines come to use.
>
> ETL stands for Extract, Transform and Load. An ETL tool extracts the data from different RDBMS source systems, real time user interactions and sever other sorts of transactions. Then the extracted data will be transformed using transformations which are almost always specific to the goal of the project like applying calculations, concatenate, analyze, and aggregate etc. And then load the data to Data Warehouse system. The data is loaded in the DW system in the form of dimension and fact tables, which can serve as the basis for which the bushiness analyzers, bushiness intelligence officers and machine learning teams can continue to work on with.

## Overview

> Our client [10 Academy](https://www.10academy.org/), recognizing the value of large data sets for speech-t0-text data sets, and seeing the opportunity that there are many text corpuses for Amharic and Swahili languages, and understanding that complex data engineering skills is valuable to our profile for employers, wants to have a design and build a robust, large scale, fault tolerant, highly available Kafka cluster that can be used to post a sentence and receive an audio file.
>
> Producing a tool that can be deployed to process posting and receiving text and audio files from and into a data lake, apply transformation in a distributed manner, and load it into a warehouse in a suitable format to train a speech-t0-text model.

## Objective

> The objective of this week’s project is to build a data engineering pipeline that allows recording millions of Amharic and Swahili speakers reading digital texts in-app and web platforms
>
> This can be achieved by building an end-to-end ETL data pipeline that will use Apache Kafka, Apache Spark and Apache Airflow in order to receive user voice audio files, transform them and load them to a data warehouse that will latter be used for text-to-speech conversion machine learning project.
>
> Users will be prompt with several different sentences and they will provide their corresponding audio by recording using the front end user interface that is provided.

## Requirements

> Python 3.5 or above
>
> Pip
>
> kafka-python
>
> Zookeeper
>
> Apache airflow
>
> Apache kafka
>
> Apache Spark

## Install

### Installing the Algorand Sandbox environment (Optional - for development use only)

```
git clone https://github.com/algorand/sandbox.git
cd sandbox
./sandbox up
```

- Detailed guidelines and instructions to develop with the Algorand sandbox could be found [here](https://github.com/algorand/sandbox)

### Installing the decentralized application

```
git clone https://github.com/Fisseha-Estifanos/algorand_dApp.git
cd algorand_dApp
pip install -r requirements.txt
```

## Examples

> ### Using the dApp

- One can start using the dApp by first cloning the repo and going to the dApp directory as shown above or can direct interact with the hosted version by going [here](https://stirring-tarsier-1ebb66.netlify.app/)

- If you choose the first option run the following command after navigating to the dApp directory to start the backend engine.

```
pip install -r requirements.txt
python algorand_dApp_back_end.py
```

- Navigate to the address provided on your local browser
- Install the AlgoSigner wallet on your browser from [here](https://chrome.google.com/webstore/detail/algosigner/kmmolakhbgdlpkjkcjkebenjheonagdm)

> #### Making transactions

- First navigate to the wallets tab.

- Start by selecting one of the provided Algorand networks as shown below.

  > ![](screenshots/select-network.png)

- After selecting networks, addresses associated with that network will be found.

- You can now easily make transactors by entering user and receiver addresses along with the amount of algos to send and some notes as shown below.

  > ![](screenshots/make-transactions.png)

- A pop up window will appear as shown below in order to grand access for the transaction. Grant the request and enter your AlgoSigner browser integration password.

  > ![](screenshots/pop-up.png)

- You can also easily check you balance as shown below.
  > ![](screenshots/get-balance.png)

> #### Creating NFT certificates

> First navigate to the NFT certificates tab.
>
> You can now create NFT certificates by entering the following parameters listed below.

- Asset name
- Asset URL
- Unit name
- Total units
- Decimals
- Note

* Note here that you first need to put your certificates in a distributed file management system, then input the address (url) of that certificate in the asset url input parameter.

  > - ![](screenshots/create-nft.png)

## Pipelines

> The decentralized application could be found here in the algorand_dApp folder.

## Notebooks

## Scripts

> All the scripts and modules for the creation of NFT certificates, transaction handling, smart contracts and any other helper scripts and modules along with default parameters and values used will be found here, in the scripts folder.

## Tests

> All the unit and integration tests are found here in the tests folder.

## Authors

> 👤 **Akubazgi Gebremariam**
>
> - Email: [Akubazgi Gebremariam](email@gamil.com)
> - GitHub: [Akubazgi Gebremariam](https://github.com/fisseha-estifanos)
> - LinkedIn: [Akubazgi Gebremariam](https://www.linkedin.com/in/fisseha-estifanos-109ba6199/)
> - Twitter: [Akubazgi Gebremariam](https://twitter.com/f0x__tr0t)

> 👤 **Birhanu Gebisa**
>
> - Email: [Birhanu Gebisa](email@gamil.com)
> - GitHub: [Birhanu Gebisa](https://github.com/fisseha-estifanos)
> - LinkedIn: [Birhanu Gebisa](https://www.linkedin.com/in/fisseha-estifanos-109ba6199/)
> - Twitter: [Birhanu Gebisa](https://twitter.com/f0x__tr0t)

> 👤 **Emtinan Salaheldin**
>
> - Email: [Emtinan Salaheldin](email@gamil.com)
> - GitHub: [Emtinan Salaheldin](https://github.com/fisseha-estifanos)
> - LinkedIn: [Emtinan Salaheldin](https://www.linkedin.com/in/fisseha-estifanos-109ba6199/)
> - Twitter: [Emtinan Salaheldin](https://twitter.com/f0x__tr0t)

> 👤 **Fisseha Estifanos**
>
> - Email: [Fisseha Estifanos](email@gamil.com)
> - GitHub: [Fisseha Estifanos](https://github.com/fisseha-estifanos)
> - LinkedIn: [Fisseha Estifanos](https://www.linkedin.com/in/fisseha-estifanos-109ba6199/)
> - Twitter: [Fisseha Estifanos](https://twitter.com/f0x__tr0t)

> 👤 **Natnael Masresha**

> - Email: [Natnael Masresha](email@gamil.com)
> - GitHub: [Natnael Masresha](https://github.com/fisseha-estifanos)
> - LinkedIn: [Natnael Masresha](https://www.linkedin.com/in/fisseha-estifanos-109ba6199/)
> - Twitter: [Natnael Masresha](https://twitter.com/f0x__tr0t)

> 👤 **Niyomukiza Thamar**
>
> - Email: [Niyomukiza Thamar](email@gamil.com)
> - GitHub: [Niyomukiza Thamar](https://github.com/fisseha-estifanos)
> - LinkedIn: [Niyomukiza Thamar](https://www.linkedin.com/in/fisseha-estifanos-109ba6199/)
> - Twitter: [Niyomukiza Thamar](https://twitter.com/f0x__tr0t)

## Show us your support

> Give us a ⭐ if you like this project, and also feel free to contact us at any moment.

![Contributors list](https://contrib.rocks/image?repo=TenAcademy/Data-Engineering_text-to-speech_data-collection)
