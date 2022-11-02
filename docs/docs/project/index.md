<script setup>
import { VPTeamMembers } from 'vitepress/theme'
import corne from '../../assets/corne.png'
import defaultPic from '../../assets/default.jpg'
import daan from '../../assets/daan.jpeg'
import laurens from '../../assets/laurens.jpeg'
import rane from '../../assets/rane.jpeg'

const members = [
  {
    avatar: 'https://avatars.githubusercontent.com/u/19239207?v=4',
    name: 'Floris van Zeeland',
    title: 'Team Lead & Developer',
    links: [
      { icon: 'github', link: 'https://github.com/nagsterFVZ' },
      { icon: 'linkedin', link: 'https://www.linkedin.com/in/florisvz/' }
    ]
  },
  {
    avatar: corne,
    name: 'Corné de Beer',
    title: 'Electronics & Power Delivery',
    links: [
      { icon: 'linkedin', link: 'https://www.linkedin.com/in/corn%C3%A9-de-beer/' }
    ]
  },
  {
    avatar: daan,
    name: 'Daan van de Ven',
    title: 'Differential & Manufacturing',
    links: [
      { icon: 'linkedin', link: 'https://www.linkedin.com/in/daanvandevennl/' }
    ]
  },
  {
    avatar: defaultPic,
    name: 'Michael Vingerhoets',
    title: 'Computer Vission & Electronics',
    links: [
      { icon: 'linkedin', link: 'https://www.linkedin.com/in/michael-vingerhoets-60b9321ab/' }
    ]
  },
  {
    avatar: defaultPic,
    name: 'Tom Leeuwen',
    title: 'Chassis & Modelling',
    // links: [
    //   { icon: 'linkedin', link: 'https://www.linkedin.com/in/corn%C3%A9-de-beer/' }
    // ]
  },
  {
    avatar: rane,
    name: 'Rane van de Pas',
    title: 'Chassis & Modelling',
    links: [
      { icon: 'linkedin', link: 'https://www.linkedin.com/in/rane-van-de-pas-a1aa75188/' }
    ]
  },
  {
    avatar: laurens,
    name: 'Laurens Nauta',
    title: 'Suspension & Chassis',
    links: [
      { icon: 'linkedin', link: 'https://www.linkedin.com/in/laurens-nauta-6024591a3/' }
    ]
  },
]
</script>

# Our Team

The team that worked on the project during our BeCreative Engineering minor at Fontys Eindhoven

<VPTeamMembers size="small" :members="members" />