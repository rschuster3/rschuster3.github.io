---
title: Brains Are Fun
layout: neuroblog/collections_layout
neuroblog_title: Learning AI Through Computational Neuroscience
---

Here we'll be covering _Theoretical Neuroscience: Computational and Mathematical MOdeling of Neural Systems_, by Peter Dayan and L. F. Abbott.

{% for post in site.neuroblog %}
  <a href="{{site.baseurl}}{{post.url}}">{{post.title}}</a>
{% endfor %}
