---
title: Learning AI Through Computational Neuroscience
layout: collections_layout
---

# Brains Are Fun
I'm getting a little bored of vanilla back end web development. Sure, building APIs and deploying them to the cloud is fun and all, but you can only do that so many times before it starts to get a little old. So I figured "Why not learn more about AI?" and, not wanting to sell myself short, decided to go way back to the basics: Computational Neuroscience. All those neural nets and reinforcement learning algorithms came from somewhere, and that somewhere was the human brain! This blog will cover Dayan and Abbot's _Theoretical Neuroscience_ textbook. I'll try to interpret the math as best I can (it's been a few years since I did muh integrals, but no reason we can't dust off the ol' [frontal cortex](https://www.sciencedirect.com/science/article/pii/S1878929317300105)). Then I'll write some code with (usually fictional) data to apply the math. We'll start simple with individual neuron firing rates and move on up to reinforcement learning models. Through this blog I hope to:
1. Make math great again (for me at least).
2. Learn about AI from first principles.
3. Hop back into scientific programming.


{% for post in site.neuroblog %}
  <a href="{{site.baseurl}}{{post.url}}">{{post.title}}</a>
{% endfor %}
