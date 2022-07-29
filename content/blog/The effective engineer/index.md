---
title: The Effective Engineer
date: 2022-07-29
math: true
diagram: true
highlight: true

toc: true

reading_time: true


image:
  preview_only: true

reading_time: true
pager: true

type: page

summary: A summary of the talk, "The Effective Engineer", by Edmond Lau. In this talk, Edmond shares about a framework called **leverage** that can be used to identify high-impact activites which produce disproportionate results.
---

I highly recommend watching the video of Edmond Lau's talk, "The Effective Engineer", to better understand the framework. This blog is supposed to serve as a quick rundown of the key information shared in the presentation.

{{< youtube BnIz7H5ruy0 >}}

### Leverage

In science, levers help us to lift a relatively heavier load with much less effort. A prominent concept called the **Pareto principle** is a formulation of this concept, 80% of the output from a given situation or system is determined by 20% of the input [^1].

{{< figure src="/blog/eff_eng_1.jpg" width="500px" title="Image from https://www.teodesk.com/blog/the-pareto-principal-are-you-wasting-80-of-your-time/">}}

In this talk, Edmond uses the term "Leverage" for tasks in the software engineering ecosystem that produces disproportionate positive results. Simply put, work that requires minimal effort and gives a greater reward.

$$Leverage = \frac{Impact \ produced}{Time \ Invested}$$

There are specific _high-leverage_ tasks in software engineering which amplify results for a given effort.

{{% callout note %}}
**High-leverage tasks:** Effective engineers use this central guiding metric to determine where and how to spend their time.
{{% /callout %}}

The key differentiating factor between a regular and highly effective developer is the ability to identify and complete such high-leverage tasks.

At times, an exciting project might not significantly impact the organization, and it is effortless to get carried away by those projects. Hence it is always important to be mindful of the time spent at work.

The following are a few of the high-leverage tasks mentioned in the video:

1. Optimize for learning and understanding

   - Taking control and ownership of your learning
   - Actionables: Reading books, taking classes, attending talks and workshops

2. Invest in iteration speed

   - Working on tasks that increase the efficiency of building pipelines; deploying services.

3. Identify and solve events or the bottlenecks that are faced during development

   - Automate or modularize a process if it is redundant more than twice.

4. Validate assumptions in increments

   - Experiment-driven product design is a potent tool
   - Breaking down large problems and building confidence from the small hypothesis; it is crucial to decompose a project into a set of testable hypotheses.

5. Minimize the operational burden

   - Code complexity: Reducing the complexity of the code is a high-leverage task
   - System complexity: Reducing the complexity of the system is a high-leverage task
   - Product complexity: when there is no clarity in the product features
   - Organizational complexity: When there are too many abstractions and team levels in an organization

6. Build a great engineering culture

   - work in environments that focus on high-leverage activities
   - optimize learning, be very productive, have good tooling and iteration speed, and hypothesis speed.
   - Strong sense of engineering culture

[^1]: https://www.techtarget.com/whatis/definition/Pareto-principle
