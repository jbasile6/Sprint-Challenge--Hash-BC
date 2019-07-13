# Sprint Challenge: Hash Tables and Blockchain

This challenge allows you to practice the concepts and techniques learned over the past week and apply them in a concrete project. This Sprint, we learned how hash tables combine two data structures to get the best of both worlds and were introduced into the fascinating world of blockchains. In your challenge this week, you will demonstrate proficiency by solving algorithms in Python using hash tables and add another key feature to your blockchain.

## Instructions

**Read these instructions carefully. Understand exactly what is expected _before_ starting this Sprint Challenge.**

This is an individual assessment. All work must be your own. Your challenge score is a measure of your ability to work independently using the material covered through this sprint. You need to demonstrate proficiency in the concepts and objectives introduced and practiced in preceding days.

You are not allowed to collaborate during the Sprint Challenge. However, you are encouraged to follow the twenty-minute rule and seek support from your PM and Instructor in your cohort help channel on Slack. Your work reflects your proficiency in Python and your command of the concepts and techniques in related to hash tables and blockchains.

You have three hours to complete this challenge. Plan your time accordingly.

## Commits

Commit your code regularly and meaningfully. This helps both you (in case you ever need to return to old code for any number of reasons and your project manager.

## Description

This sprint challenge is divided up into three parts:  Hash tables (24 points), blockchain (12 points) and a short interview (20 points). There is also a stretch goal in the blockchain section which should only be attempted after the rest of the problems have been completed.

## Interview Questions

During your challenge, you will be pulled aside by a PM for a 5 minute interview. During this interview, you will be expected to answer the following three questions:

  * 1. What is a blockchain and how does it work?

A blockchain is a secure data structure. It is has no centralized authority. It is available to anyone and many people must use it and share data between other holders of the block chain for to be effective. The chain must begin with a genesis block. Each block in the chain is a collection of information.

A block is created when a proof is found for a block. Proofs are a hashed version of the guess and last block proofs. Proofs must meet a certain condition. In the examples we've done the condition has been that the first 4 or 6 letters of the hashed guess equals '0000'/'000000'. When a block is created it contains the pending transaction, the proof, and a hash of the previous block. When the new block is created, it is sent to each node, a person holding the chain, and needs to be accepted and verified by the other nodes to be added to the chain. This makes it so the blocks within the chain are immutable.

  * 2. What is an array and how does it work?

An array is the most basic type of data structure. It is just a contiguous block of data in storage. An array holds a fixed number of values of any data type. An array is useful because you have direct access to the index of the list as opposed to something like a linked list, which sends each node to another point memory and does not give access to each index of the list.

  * 3. What is a hash table and how does it work?

A hash table is similar to an array. It also its a contiguous block of data. A hash table is more complex than an array and the data is not simply listed. It uses a hash function to compute an index into an array. The data is stored as a key: value pair. The keys run through the hashing function and give an output of a number between 0 and the desired length of the table. The value is placed in the index the hashing function returns. If we want to find that value we simply run the key ack through the hashing function to get the index.

Hash tables have whats called a collision when two keys have the same outputted index. To avoid this we have to make sure we resize the table whenever it is nearing capacity.

You will receive points at the PM's discretion based on the following criteria:

  * 20: Would love to have this person on my team!
  * 14: Wouldn't mind working with this person.
  * 10: Knowledge is lacking OR poor communication skills
  *  6: Knowledge is lacking AND poor communication skills
  *  2: You get 2 points for showing up



## Project Set Up

#### [Hash Tables]

For the hash tables portion of the sprint challenge, you'll be working through two algorithm problems that are amenable to being solved efficiently using a hash table. You know the drill at this point. Navigate into each exercise's directory, read the instructions for the exercise laid out in the README, implement your solution in the .py skeleton file, then make sure your code passes the tests by running the test script with make tests.

A hash table implementation has been included for you already. Your task is to get the tests passing (ideally using a hash table to do it). You can remind yourself of what hash table functions are available by looking at the hashtable.py file that is included in each exercise directory (note that the hash table implementations for both exercises differ slightly).

*You may not use any advanced built-in Python functions to solve these problems.*

#### [Blockchain]

For the blockchain portion of the challenge, you will be writing code for a new miner that will solve a different Proof of Work algorithm than the one we have been working with.

Your goal is to mine at least one coin.  Keep in mind that with many people competing over the same coins, this may take a long time.  By our math, we expect that an average solution should be the first to find a solution at least once in an hour or two of mining.  

## Minimum Viable Product

You can earn 35 points from the main coding portion of the sprint challenge.  Be sure to budget your time wisely.  The Blockchain challenge is fun, but it is only 1/3 of the points availible for the coding portion of this challenge.  

#### [Blockchain](https://github.com/LambdaSchool/Sprint-Challenge--Hash-BC/tree/master/blockchain) - 12 pts
  * ex1 - 12 pts

#### [Hash Tables](https://github.com/LambdaSchool/Sprint-Challenge--Hash-BC/tree/master/hashtables) - 24 pts
  * ex1 - 12 pts
  * ex2 - 12 pts

Both Hash Table problems will be graded as follows:
  * 1: Code attempted
  * 2: Code resembles the correct solution
  * 3: Tests pass
  * 4: Tests pass, using the existing hash table implementation, no flake8 complaints
  * 5: Tests pass, using the existing hash table implementation, no flake8 complaints, linear runtime complexity


### Grading

Students can receive up to 55 points in total for this Sprint Challenge (not including 4 extra credit points). 

  * __Challenge__: 35
  * __Interview__: 20

--------

The score distributions are as follows:

  * __3__: >= 48 points
  * __2__: >= 35 points
  * __1__: < 34 points 
